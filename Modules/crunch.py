from Modules import tools
from Modules import constants

__author__ = 'Gus'


def crf(path, level):
    tempPath = tools.getTempFilePath(path, '.mp4')
    path = tools.shellQuote(path)
    tempPath = tools.shellQuote(tempPath)
    command = tools.createCommand(constants.FFMPEG_CRF, path, tempPath)
    command = command.replace(constants.CRF_PLACEHOLDER, level)
    return tools.runSystemCommand(command)
	
def crfandstream(path, level):
    tempPath = tools.getTempFilePath(path, '.mp4')
    path = tools.shellQuote(path)
    tempPath = tools.shellQuote(tempPath)
    command = tools.createCommand(constants.FFMPEG_OPT_CRF_AND_STREAM, path, tempPath)
    command = command.replace(constants.CRF_PLACEHOLDER, level)
    return tools.runSystemCommand(command)