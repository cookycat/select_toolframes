from vcCommand import *
from vcHelpers.Selection import *


def selectToolFrames(prop):
    app = getApplication()
    sm = app.SelectionManager
    tool_frames = getAllToolFrames()
    selection = sm.setSelection(tool_frames)


def getAllToolFrames():
    if not component.Value:
        return
    behaviors = getGivenComponentsBehaviours(component.Value)
    tool_containers = filterBehaviours(behaviors, VC_TOOLCONTAINER)
    
    robot_controllers = filterBehaviours(behaviors, VC_ROBOTCONTROLLER)
    
    frames = []
    if tool_containers:
        for tools in tool_containers:
            frames.extend(tools)
    elif robot_controllers:
        for rc in robot_controllers:
            frames.extend(rc.Tools)
    return frames


def first_state():
    executeInActionPanel()


cmd = getCommand()
component = cmd.createProperty("Ref<Component>", "Component")
select_btn = cmd.createProperty(VC_BUTTON, "Select")
select_btn.OnChanged = selectToolFrames
addState(first_state)