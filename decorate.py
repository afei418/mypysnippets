#!/usr/bin/python

from time import time
def costTime(func):
    def result(*argv, **args):
        begin = time()
        func(*argv, **args)
        print("cost time: %s" % (time() - begin))
    return result

@costTime
def show(n):
    for x in range(n):
        print(x)

if __name__ == "__main__":
    num = int(raw_input("Enter a number:"))
    show(num)
