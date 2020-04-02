#!/usr/bin/env python3
import subprocess
import sys
sep = b'__APERTIUM_INTERNAL_FIELD_SEPARATOR__'
strings = [ text.decode('utf-8') for text in sys.stdin.buffer.read().split(sep) ]
for string in strings:
    print(string)
