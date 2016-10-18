# ProVids
Converts, Compresses and Optimizes Videos for Streaming over the Internet
### WARNING - Only works on Windows at the moment, adding cross platform support soon.
##Overview
Takes a folder of videos and runs a set of ffmpeg commands on every video that i have found to be ideal for streaming over the internet,
then sends the output to a chosen folder.
## Windows
Run the following command:
```
path\to\provids.bat path\to\videos\folder path\to\destination\folder
```
To make life easier, add provids.bat as environment variable to your system, then its just:
```
provids path\to\videos\folder path\to\destination\folder
```
As it stands provids takes no arguments (See to do below), so the following defaults are used:
* CRF - 21
* Output container - .mp4
* Minimum Size for Compression - 2GB

## To Do
* Add linux and mac support
* Add arguments to set above variables

## Cons
* Only supports .mkv, .m4a and .mov files as they are easily interchangable with mp4
