#!/usr/bin/python

import cmd
import re
import timestamp

stats = cmd.run('speedtest-cli')

# Example:
# Download: 38.87 Mbits/s
# Upload: 5.29 Mbits/s

download = re.compile( r'Download: ([0-9]*\.[0-9]*.*)\n').findall(stats)
if len(download) > 0:
    download = download[0]
else:
    download = "ERROR"


upload = re.compile( r'Upload: ([0-9]*\.[0-9]*.*)\n').findall(stats)
if len(upload) > 0:
    upload = upload[0]
else:
    upload = "ERROR"


time = timestamp.now()

string = time + ', ' + download + ', ' + upload

f = open("speedLog.txt", 'a')
f.write(s + "\n")
f.close()
