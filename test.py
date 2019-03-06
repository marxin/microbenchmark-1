#!/usr/bin/env python3

import os
import sys
import random
import subprocess
import time

tests = [8, 16, 32, 64, 128, 256, 1024, 2048, 4096]
runs = 1

def test(i, options):
    subprocess.check_output('gcc gen%d.c main.c -O2 %s' % (i, options), shell = True)

    times = []
    for x in range(runs):
        start = time.time()
        subprocess.check_output('./a.out', shell = True)
        end = time.time()
        times.append(end - start)

    return sum(times) / len(times)

print('             normal       retpoline    retpo+no-JT  retpo+JT=20  retpo+JT=40')
for i in tests:
    subprocess.check_output('./gen.py %d > gen%d.c' % (i, i), shell = True)
    results = []
    results.append(test(i, ''))
    results.append(test(i, '-mindirect-branch=thunk'))
    results.append(test(i, '-mindirect-branch=thunk -fno-jump-tables'))
    results.append(test(i, '-mindirect-branch=thunk --param case-values-threshold=20'))
    results.append(test(i, '-mindirect-branch=thunk --param case-values-threshold=40'))

    print('cases: %4d:' % i, end = '')
    for r in results:
        print('%5.2f (%3.0f%%) ' % (r, 100 * r / results[0]), end = '')
    print()
