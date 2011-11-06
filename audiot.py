#!/usr/bin/env python2

"""
This is a simple python script to convert music from flac to
various other lossy audio formats.
It is Open Source.
"""


#A bit of parsing
from optparse import OptionParser
parser = OptionParser(usage=__doc__, version='1')
parser.add_option('-h', '--hosts', dest='HOSTS', default=None, help="Specifies a custom hosts file")
(opts, args) = parser.parse_args()

