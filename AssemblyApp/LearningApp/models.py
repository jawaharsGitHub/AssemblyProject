#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.db import models

வணக்கம் = 'hello'
print(வணக்கம்)

# hi\
# hi
if 10 > 5 \
        and 11 > 5 \
        and 11 > 5:
    print('ok')

    print('123456'
          '789')

    month_names = ['one', 'two'  # hi

        , 'three']

    print(month_names)

if 5 < 6:
    print('y1')
else:
    print('n')

if 5 < 6:
    print('y2')
else:
    print('n')


# Create your models here.

def perm(l):
    # Compute the list of all permutations of l
    if len(l) <= 1:
        return [l]
    r = []
    for i in range(len(l)):
        s = l[:i] + l[i + 1:]
        p = perm(s)
        for x in p:
            r.append(l[i:i + 1] + x)
    return r


# print(perm('1234'))

def perm2(l):  # error: first line indented
    r = []
    for i in range(len(l)):  # error: not indented
        s = l[:i] + l[i + 1:]
        p = perm(l[:i] + l[i + 1:])  # error: unexpected indent
        for x in p:
            r.append(l[i:i + 1] + x)
    return r  # error: inconsistent dedent


print(perm2('1234'), len(perm2('1234')))

a, b = 0, 1
