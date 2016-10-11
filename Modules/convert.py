import tools
import constants

__author__ = 'Gus'


def toMP4(path):
    tempPath = tools.getTempFilePath(path, '.mp4')
    path = tools.shellQuote(path)
    tempPath = tools.shellQuote(tempPath)
    command = tools.createCommand(constants.FFMPEG_CONVERT, path, tempPath)
    return tools.runSystemCommand(command)


