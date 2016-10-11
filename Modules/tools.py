import os
import time
from glob import glob

import shutil

import constants

__author__ = 'Gus'


def shellQuote(path):
    return "\"" + path + "\""


def unShellQuote(path):
    return path.replace("\"", "")


def secondTimer(seconds):
    time.sleep(1000 * seconds)


def minuteTimer(minutes):
    time.sleep(60000 * minutes)


def hourTimer(hours):
    time.sleep(3600000 * hours)


def getFileNamesRecursive(path, type):
    return [y for x in os.walk(path) for y in glob(os.path.join(x[0], type))]


def getFileSize(path):
    return os.path.getsize(path)


def megabytes(megs):
    return megs * 1000000


def gigabytes(gigs):
    return gigs * 1000000000


def runSystemCommand(command):
    return os.system(command)


def move(src, dst):
    shutil.move(src, dst)


def rename(path, name):
    os.rename(path, name)


def remove(path):
    os.remove(path)


def getPathWithoutExtension(path):
    periodIndex = path.rfind('.')
    return path[0:periodIndex]


def getBasenameWithoutExtension(path):
    path = getPathWithoutExtension(path)
    return path.split(os.sep)[len(path.split(os.sep))-1]

def getExtension(path):
    periodIndex = path.rfind('.')
    return path[periodIndex:len(path)]


def getTempFilePath(path, extension):
    oldExtension = getExtension(path)
    oldBasename = getBasenameWithoutExtension(path)
    newBasename = oldBasename + constants.TEMP_FILE_EXTRA
    return path.replace(oldBasename, newBasename).replace(oldExtension, extension)


def currentDir():
    return os.path.dirname(os.path.realpath(__file__))


def getOriginalFilenameFromTemp(filename):
    return filename.replace(constants.TEMP_FILE_EXTRA, '')


def getFFMPEGPath():
    for i in range(0, len(constants.FFMPEG_PATHS)):
        try:
            candidate = os.path.join(currentDir(), constants.FFMPEG_PATHS[i])
            if os.path.exists(candidate):
                return candidate
        except ValueError:
            continue

    return 'FFMPEG NOT FOUND'


def createCommand(command, input, output):
    return getFFMPEGPath() + command \
        .replace(constants.INPUT_PLACEHOLDER, input) \
        .replace(constants.OUTPUT_PLACEHOLDER, output)
