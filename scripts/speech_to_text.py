#!/usr/bin/python

import urllib2
import json
import sys
import os

def speech_to_txt(flac_filename):
  print "CONTACTING GOOGLE SPEECH API"
  url = "https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&lang=en-US"
  audio = open(flac_filename, 'rb').read()
  headers = {'Content-Type': 'audio/x-flac; rate=16000', 'User-Agent':'Mozilla/5.0'}
  request = urllib2.Request(url, data=audio, headers=headers)
  response = urllib2.urlopen(request)
  r = response.read()
  print "Response: %s"%(r)
  try:
    return json.loads(r)
  except ValueError:
    print "Speech API json.loads ValueError"
    return json.loads(json.dumps({}))

def usage():
  return "python speech_to_text.py <path_to_flac_file>"

if __name__ == "__main__":
  if (len(sys.argv) < 2):
    print usage()
    exit(-1)
  filename = sys.argv[1]
  #should add a check that filename is if extension .flac
  fname, fileExtension = os.path.splitext(filename)
  if (fileExtension != '.flac'):
    print usage()
    exit(-1)
  r = speech_to_txt(filename)
