# Spot Python SDK 5.2.0: selected command API documentation

Selected documentation set, not an exhaustive Spot capability list. Original docstrings obtained from installed bosdyn-client 5.2.0.

## RobotCommandBuilder.synchro_stand_command

Signature: synchro_stand_command(params=None, body_height=0.0, footprint_R_body=<EulerZXY default; object address omitted>, build_on_command=None)

Command robot to stand. If the robot is sitting, it will stand up. If the robot is
moving, it will come to a stop. Params can specify a trajectory for the body to follow while
standing. In the simplest case, this can be a specific position+orientation which the body
will hold at. The arguments body_height and footprint_R_body are ignored if params argument
is passed.

Args:
    params(spot.MobilityParams): Spot specific parameters for mobility commands. If not set,
        this will be constructed using other args.
    body_height(float): Height, meters, to stand at relative to a nominal stand height.
    footprint_R_body(EulerZXY): The orientation of the body frame with respect to the
        footprint frame (gravity aligned framed with yaw computed from the stance feet)
    build_on_command: Option to input a RobotCommand (not containing a full_body_command). An
        arm_command and gripper_command from this incoming RobotCommand will be added
        to the returned RobotCommand.

Returns:
    RobotCommand, which can be issued to the robot command service.

## RobotCommandBuilder.synchro_sit_command

Signature: synchro_sit_command(params=None, build_on_command=None)

Command the robot to sit.

Args:
    params(spot.MobilityParams): Spot specific parameters for mobility commands.
    build_on_command: Option to input a RobotCommand (not containing a full_body_command). An
        arm_command and gripper_command from this incoming RobotCommand will be added
        to the returned RobotCommand.

Returns:
    RobotCommand, which can be issued to the robot command service.

## RobotCommandBuilder.stop_command

Signature: stop_command()

Command to stop with minimal motion. If the robot is walking, it will transition to
stand. If the robot is standing or sitting, it will do nothing.

Returns:
    RobotCommand, which can be issued to the robot command service.

## RobotCommandBuilder.synchro_velocity_command

Signature: synchro_velocity_command(v_x, v_y, v_rot, params=None, body_height=0.0, locomotion_hint=1, frame_name='body', build_on_command=None)

Command robot to move along 2D plane. Velocity should be specified in the robot body
frame. Other frames are currently not supported. The arguments body_height and
locomotion_hint are ignored if params argument is passed.

A velocity command requires an end time. End time is not set in this function, but rather
is set externally before call to RobotCommandService.

Args:
    v_x: Velocity in X direction.
    v_y: Velocity in Y direction.
    v_rot: Velocity heading in radians.
    params(spot.MobilityParams): Spot specific parameters for mobility commands. If not set,
        this will be constructed using other args.
    body_height: Height, meters, relative to a nominal stand height.
    locomotion_hint: Locomotion hint to use for the velocity command.
    frame_name: Name of the frame to use.
    build_on_command: Option to input a RobotCommand (not containing a full_body_command). An
        arm_command and gripper_command from this incoming RobotCommand will be added
        to the returned RobotCommand.

Returns:
    RobotCommand, which can be issued to the robot command service.

## RobotCommandBuilder.synchro_se2_trajectory_point_command

Signature: synchro_se2_trajectory_point_command(goal_x, goal_y, goal_heading, frame_name, params=None, body_height=0.0, locomotion_hint=1, build_on_command=None)

Command robot to move to pose along a 2D plane. Pose can be specified in the world
(kinematic odometry) frame or the robot body frame. The arguments body_height and
locomotion_hint are ignored if params argument is passed.

A trajectory command requires an end time. End time is not set in this function, but rather
is set externally before call to RobotCommandService.

Args:
    goal_x: Position X coordinate.
    goal_y: Position Y coordinate.
    goal_heading: Pose heading in radians.
    frame_name: Name of the frame to use.
    params(spot.MobilityParams): Spot specific parameters for mobility commands. If not set,
        this will be constructed using other args.
    body_height: Height, meters, relative to a nominal stand height.
    locomotion_hint: Locomotion hint to use for the trajectory command.
    build_on_command: Option to input a RobotCommand (not containing a full_body_command). An
        arm_command and gripper_command from this incoming RobotCommand will be added
        to the returned RobotCommand.

Returns:
    RobotCommand, which can be issued to the robot command service.

## RobotCommandBuilder.selfright_command

Signature: selfright_command()

Command to get the robot in a ready, sitting position. If the robot is on its back, it
will attempt to flip over.

Returns:
    RobotCommand, which can be issued to the robot command service.

