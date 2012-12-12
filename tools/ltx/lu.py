#!/usr/bin/python

import sys
w = sys.stdout.write

data = dict()

def getstat(ls):
    assert(len(ls) == 10)
    avg = 0
    for i in range(len(ls)):
        avg += float(ls[i])
    avg /= len(ls)
    dev = 0
    for i in range(len(ls)):
        dev += (float(ls[i]) - avg) ** 2
    dev /= len(ls) - 1
    dev **= .5
    return avg, dev


def readfile(n):
    global data
    f = "../../LU/pthread%d" % n
    fl = open(f)
    lines = fl.readlines()
    for i in range(int(len(lines) / 11)):
        ls = lines[11*i].split(" ")
        arr = data.get(ls[2], [])
        avg, dev = getstat(lines[11*i+1:11*(i+1)])
        arr.append([avg, dev])
        data[ls[2]] = arr

for i in range(4):
    readfile(2 ** i)

keys = data.keys()
keys = sorted(keys, key=lambda x: int(x[:x.index('x')]))
print(keys)
for sz in keys:
    at = data[sz]
    for i in range(4):
        w("%.6f $\pm$ %.6f" % (at[i][0], at[i][1]))
        if 3 == i:
            w(" \\")
        else:
            w(" & ")
    w("\n")

