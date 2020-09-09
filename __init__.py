from vcApplication import *

def OnAppInitialized():
    cmduri = getApplicationPath() + "select_tool_frames.py"
    cmd = loadCommand("selectToolFrames", cmduri)
    addMenuItem("VcTabTeach/Helpers", "Tool Frames", -1, "selectToolFrames")