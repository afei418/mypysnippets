#!/usr/bin/python 

import os
import shutil
import glob
import sys
import getopt
import argparse
import re
import math
import random

print(glob.glob('/home/ninameng/pyproject/*.py'))

#shutil.copy()
#shutil.move()

os.getcwd()
os.chdir('/home/ninameng/pyproject')
os.system('ls -l')

print(sys.argv)
sys.stderr.write("Error")

re.findall(r'\bf[a-z]*', 'which foot or hand fell faster')
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

math.cos(math.pi /4.0)
math.log(1024, 2)
random.random()


sys.exit()
