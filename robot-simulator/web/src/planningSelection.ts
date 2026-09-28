/** Selection changes preserve every currently satisfied capability minimum. */
export type PlanningRequirement = {
  id: string;
  min_count: number;
  eligible_robot_ids: string[];
  alternative_robot_ids?: string[];
};

const count = (ids: string[], requirement: PlanningRequirement) =>
  new Set(ids.filter((id) => requirement.eligible_robot_ids.includes(id))).size;

export function canRemovePlanningRobot(
  ids: string[],
  requirements: PlanningRequirement[],
  robotId: string,
): boolean {
  if (!ids.includes(robotId)) return true;
  const next = ids.filter((id) => id !== robotId);
  return requirements.every((requirement) => {
    if (!Number.isInteger(requirement.min_count) || requirement.min_count < 0)
      return false;
    // An already incomplete draft must not lose further required capacity.
    return (
      count(next, requirement) >=
      Math.min(requirement.min_count, count(ids, requirement))
    );
  });
}

export function swapPlanningRobot(
  ids: string[],
  requirements: PlanningRequirement[],
  requirementId: string,
  replacement: string,
  assignedRobotId?: string,
): { robotIds: string[]; retainedRobotIds: string[]; reason: string | null } {
  const original = [...new Set(ids)];
  const requirement = requirements.find((row) => row.id === requirementId);
  if (
    !requirement ||
    !(
      requirement.alternative_robot_ids ?? requirement.eligible_robot_ids
    ).includes(replacement)
  )
    return {
      robotIds: original,
      retainedRobotIds: [],
      reason: "이 역할에 사용할 수 있는 대체 로봇이 아닙니다.",
    };
  const previous =
    assignedRobotId && original.includes(assignedRobotId)
      ? assignedRobotId
      : requirement.eligible_robot_ids.find((id) => original.includes(id));
  const next = [...new Set([...original, replacement])];
  if (!previous || previous === replacement)
    return { robotIds: next, retainedRobotIds: [], reason: null };
  const revisedRequirements = requirements.map((row) =>
    row.id === requirementId
      ? {
          ...row,
          eligible_robot_ids:
            row.alternative_robot_ids ?? row.eligible_robot_ids,
        }
      : row,
  );
  if (!canRemovePlanningRobot(next, revisedRequirements, previous))
    return {
      robotIds: next,
      retainedRobotIds: [previous],
      reason:
        "기존 로봇이 다른 필수 역할이나 최소 대수에 필요해 함께 유지했습니다.",
    };
  return {
    robotIds: next.filter((id) => id !== previous),
    retainedRobotIds: [],
    reason: null,
  };
}
