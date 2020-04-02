#!/usr/bin/env python3
import subprocess
import sys
sep = b'__APERTIUM_INTERNAL_FIELD_SEPARATOR__'
command = sys.argv[1]
byteses = sys.stdin.buffer.read().split(sep)
sys.stdout.buffer.write(sep.join([ subprocess.check_output(command, input=chunk, shell=True) for chunk in byteses ]))
