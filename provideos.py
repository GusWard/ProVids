import os
import sys
import stat

from send2trash import send2trash

from Modules import tools
from Modules import convert
from Modules import crunch
from Modules import optimise

__author__ = 'Gus'


def validateArguments(arguments):
    if len(arguments) < 3:
        print 'Please provide a folder to process, and a target folder.'
        exit(0)
    if len(arguments) > 3:
        print 'Please only provide a folder to process, and a target folder.'
        print 'e.g. python processvideosrelocate.py inputfolder outputfolder'
        exit(0)
    if not os.path.exists(arguments[1]):
        print 'Input folder does not exist'
        exit(0)
    if not os.path.exists(arguments[2]):
        print 'Output folder does not exist'
        exit(0)

if __name__ == "__main__":

    paths = sys.argv
    validateArguments(paths)

    sourcePaths = paths[1]
    targetPath = paths[2]

    videofiles = tools.getFileNamesRecursive(sourcePaths, "*.mkv")
    videofiles.extend(tools.getFileNamesRecursive(sourcePaths, "*.mov"))
    videofiles.extend(tools.getFileNamesRecursive(sourcePaths, "*.m4a"))
    videofiles.extend(tools.getFileNamesRecursive(sourcePaths, "*.mp4"))
    videofiles.extend(tools.getFileNamesRecursive(sourcePaths, "*.avi"))

    print 'Found videos:'
    print "\n".join(videofiles)

    for i in range (0, len(videofiles)):
    
        needsConvert = False
        needsCompress = False
    
        print 'Processing new video - ' + os.path.basename(videofiles[i])
        finalFilename = ''
        tempfilename = tools.getTempFilePath(videofiles[i], '.mp4')
        finalFilename = tools.getOriginalFilenameFromTemp(tempfilename)
        os.chmod(videofiles[i], stat.S_IRWXU)
		
        needsConvert = True

        if tools.getFileSize(videofiles[i]) > tools.gigabytes(2):
            needsCompress = True
        else:
            print 'Video too small to compress.'
		
        if needsConvert:
            print 'Attempting to convert to MP4 using libx264, aac...'
            if convert.toMP4(videofiles[i]) == 0:
                send2trash(videofiles[i])
                tools.rename(tempfilename, finalFilename)
                print 'Success!'
            else:
                finalFilename = videofiles[i]
                if os.path.exists(tempfilename):
                    send2trash(tempfilename)
                print 'Failed!'
		
        if needsCompress:
		
            print 'Attempting to compress video and optimise for streaming...'
            if crunch.crfandstream(finalFilename, "21") == 0:
                send2trash(finalFilename)
                tools.rename(tempfilename, finalFilename)
                print 'Success!'
            else:
                if os.path.exists(tempfilename):
                    send2trash(tempfilename)
                print 'Failed!'
		
        else:
		
            print 'Attempting to optimise for streaming...'
            if optimise.forStreaming(videofiles[i].replace(tools.getExtension(videofiles[i]), ".mp4")) == 0:
                send2trash(videofiles[i].replace(tools.getExtension(videofiles[i]), ".mp4"))
                tools.rename(tempfilename, finalFilename)
                print 'Success!'
            else:
                finalFilename = videofiles[i]
                if os.path.exists(tempfilename):
                    send2trash(tempfilename)
                print 'Failed!'

        print 'Moving to target location...'
        tools.move(finalFilename, targetPath)
        print 'Complete!'
