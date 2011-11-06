#!/usr/bin/env python2
from glob import glob
from optparse import OptionParser

"""
This is a simple python script to convert music from flac to
various other lossy audio formats.
It is Open Source.
"""


#A bit of parsing
parser = OptionParser(usage=__doc__, version='1')
parser.add_option('-i', '--interactive', action='store_true', dest='INTER', default=False, help='Should the script run in an interactive mode?')
parser.add_option('-f', '--hosts-file', dest='HOSTS', default=None, help="Specifies a custom hosts file")
(opts, args) = parser.parse_args()

import fnmatch
import os

matches = []
for root, dirnames, filenames in os.walk('/home/sauron/muzyka'):
  for filename in fnmatch.filter(filenames, '*.mp3'):
      matches.append(os.path.join(root, filename))
for match in matches:
    print match
