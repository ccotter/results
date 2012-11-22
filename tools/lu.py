#!/usr/bin/python

import sys

def readfile(n, blksize):
    f = "../LU/%d/%dx%d" % (n, blksize, blksize)
    fl = open(f)
    lines = fl.readlines()
    print("N=%d %dx%d" % (n, blksize, blksize))
    for i in range(int(len(lines) / 2)):
        sz = lines[2*i].split(" ")[2]
        t = float(lines[2*i+1].split(":")[1])
        print("%s,%f" % (sz,t))
    print()

toread = [
    [
        [1, 16],
        [1, 32],
        [1, 64],
        [1, 128]
    ],
    [
        [2, 16],
        [2, 32],
        [2, 64],
        [2, 128]
    ],
    [
        [4, 16],
        [4, 32],
        [4, 64],
        [4, 128]
    ],
    [
        [8, 16],
        [8, 32],
        [8, 64],
        [8, 128]
    ],
]

for i in range(len(toread)):
    for j in range(len(toread[i])):
        readfile(toread[i][j][0], toread[i][j][1])


