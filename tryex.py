#!/usr/bin/python

try:
    var = int(raw_input("Input a number:"))
except(ValueError):
    print("Not number!")
else:
    print("You input %d" %  var)
finally:
    print("Finish!")

