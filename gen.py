#!/usr/bin/env python3

import os
import sys
import random

random.seed(0)

N = int(sys.argv[1])

print('int global;')
print('int foo (int x) {')
print('switch (x & %d) {' % (N - 1))

for i in range(N):
    print('  case %d: %s; return %d;' % (i, 'global += %d' % i if random.randrange(10) == 0 else '', random.randrange(2222)))

print('  default: return 0;')
print('}}')
