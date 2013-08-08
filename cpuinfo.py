#!/usr/bin/env python

from __future__ import print_function
from collections import OrderedDict
import pprint

def cinf():
    with open('/proc/cpuinfo') as cinf:
        for line in cinf:
            print(line.rstrip('\n'))

def cmodel():
    with open('/proc/cpuinfo') as cinf:
        for line in cinf:
            if line.strip():
                if line.rstrip('\n').startswith('model name'):
                    model_name = line.rstrip('\n').split(':')[1]
                    print(model_name)

def carch():
    with open('/proc/cpuinfo') as cinf:
        for line in cinf:
            if line.strip():
                line = line.rstrip('\n')
                if line.startswith('flags') or line.startswith('Features'):
                    if 'lm' in line:
                        print('64 bit')
                    else:
                        print('32 bit')

def dictcinf():
    ''' Return the information in /proc/cpuinfo as a dictionary in the
    following format:
    cpu_info['proc0'] = {....}
    cpu_info['proc1'] = {....} '''

    cpuinfo = OrderedDict()
    procinfo = OrderedDict()

    nprocs = 0
    with open('/proc/cpuinfo') as cinf:
        for line in cinf:
            if not line.strip():
                cpuinfo['proc%s' % nprocs] = procinfo
                nprocs += 1
                procinfo = OrderedDict() #reset
            else:
                if len(line.split(':')) == 2:
                    procinfo[line.split(':')[0].strip()] = line.strip(':')[1].strip()
                else:
                    procinfo[line.split(':')[0].strip()] = ''
    return cpuinfo

if __name__ == '__main__':
#    cinf()
#    cmodel()
#    carch()
    cpuinfo = dictcinf()
    for processor in cpuinfo.keys():
        print(cpuinfo[processor]['model name'])
