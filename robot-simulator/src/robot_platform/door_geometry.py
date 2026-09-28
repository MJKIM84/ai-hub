"""Authored door actuation, shared by model compilation and runtime control."""
def door_geometry(element, environment_id):
    motion=element.facility.door_motion or ('vertical' if environment_id.startswith('floorplan-') else 'normal')
    return dict(motion=motion,axis={'vertical':'0 0 1','lateral':'1 0 0','normal':'0 1 0'}[motion],
                travel=element.size.z+.5 if motion=='vertical' else element.size.x+.1 if motion=='lateral' else element.size.x)
