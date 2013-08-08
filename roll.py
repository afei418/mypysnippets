import random
import sys

if len(sys.argv) <= 1:
    range = 100
else:
    range = int(sys.argv[1])
#if sys.argv[1] != Null

number = random.randint(1,range)
print("Sleepd roll is {0}:(1 - {1})".format(number, range))