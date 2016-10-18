import os

__author__ = 'Gus'

VIDEO_FILE_TYPES = ['*.mp4', '*.mov', '*.mkv', '*.m4a']

TEMP_FILE_EXTRA = "-temp"

SCRAP_FILE_PATH = "scrapheap" + os.sep

FFMPEG_PATHS = ['Res' + os.sep + 'bin' + os.sep + 'ffmpeg.exe', '..' + os.sep + 'Res' + os.sep + 'bin' + os.sep + 'ffmpeg.exe', '..' + os.sep + '..' + os.sep + 'Res' + os.sep + 'bin' + os.sep + 'ffmpeg.exe']

INPUT_PLACEHOLDER = '$INPUT'

OUTPUT_PLACEHOLDER = '$OUTPUT'

CRF_PLACEHOLDER = '$CRF'

# -loglevel quiet

FFMPEG_CONVERT = ' -threads 0 -i ' + INPUT_PLACEHOLDER + ' -loglevel quiet -vcodec libx264 -acodec aac -preset slower ' + OUTPUT_PLACEHOLDER

FFMPEG_CRF = ' -threads 0 -i ' + INPUT_PLACEHOLDER + ' -loglevel quiet -vcodec copy -acodec copy -preset slower -crf ' + CRF_PLACEHOLDER + ' ' + OUTPUT_PLACEHOLDER

FFMPEG_OPT_STREAM = ' -threads 0 -i ' + INPUT_PLACEHOLDER + ' -loglevel quiet -movflags faststart -acodec copy -vcodec copy -preset slower ' + OUTPUT_PLACEHOLDER

FFMPEG_OPT_CRF_AND_STREAM = ' -threads 0 -i ' + INPUT_PLACEHOLDER + ' -loglevel quiet -vcodec copy -acodec copy -movflags +faststart -preset slower -crf ' + CRF_PLACEHOLDER + ' ' + OUTPUT_PLACEHOLDER
