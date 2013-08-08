#!/usr/bin/env python

import platform

def pftest():
    print(platform.uname()[1])
    # In python3, reture a named tuple: uname_result(system='Linux', ...)
    print(platform.system())      #property interface
    print(platform.release())
    print(platform.linux_distribution())
    print(platform._supported_dists)
    print(platform.architecture())


if __name__ == '__main__':
    pftest()
