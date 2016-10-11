from Modules import tools
from Modules import constants

__author__ = 'Gus'

def forStreaming(path):
    tempPath = tools.getTempFilePath(path, '.mp4')
    path = tools.shellQuote(path)
    tempPath = tools.shellQuote(tempPath)
    command = tools.createCommand(constants.FFMPEG_OPT_STREAM, path, tempPath)
    return tools.runSystemCommand(command)