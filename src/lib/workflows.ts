const STORAGE_KEY = "pipeai_workflows";
const MAX_STAGES = 10;

export interface WorkflowStage {
  serviceId: string;
  serviceName: string;
  serviceCategory: string;
  serviceLogo?: string;
}

export interface SavedWorkflow {
  name: string;
  stages: WorkflowStage[];
  createdAt: string;
}

export function saveWorkflow(name: string, stages: WorkflowStage[]): void {
  const workflows = loadWorkflows();
  const existing = workflows.findIndex((w) => w.name === name);
  const entry: SavedWorkflow = {
    name,
    stages: stages.slice(0, MAX_STAGES),
    createdAt: new Date().toISOString(),
  };
  if (existing >= 0) {
    workflows[existing] = entry;
  } else {
    workflows.push(entry);
  }
  localStorage.setItem(STORAGE_KEY, JSON.stringify(workflows));
}

export function loadWorkflows(): SavedWorkflow[] {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

export function deleteWorkflow(name: string): void {
  const workflows = loadWorkflows().filter((w) => w.name !== name);
  localStorage.setItem(STORAGE_KEY, JSON.stringify(workflows));
}

export function encodeWorkflow(stages: WorkflowStage[]): string {
  return btoa(encodeURIComponent(JSON.stringify(stages.map((s) => s.serviceId))));
}

export function decodeWorkflow(hash: string): string[] {
  try {
    return JSON.parse(decodeURIComponent(atob(hash)));
  } catch {
    return [];
  }
}

export { MAX_STAGES };
