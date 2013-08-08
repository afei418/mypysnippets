#!/usr/bin/env python

'''List of all the process IDs currently active'''

from __future__ import print_function
import os

def procslst():
    pids = []
    for subdir in os.listdir('/proc'):
        if subdir.isdigit():
            pids.append(subdir)

    return pids

if __name__ == '__main__':
    pids = procslst()
    print('Total numbers of runing process::{0}'.format(len(pids)))
