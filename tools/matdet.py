#!/usr/bin/python

# To format pthread matmult evals into CSV format.

def getstat(ls):
    assert(len(ls) == 10)
    avg = [0,0]
    for i in range(len(ls)):
        at = ls[i].split(" ")
        avg[0] += float(at[0])
        avg[1] += float(at[1])
    avg[0] /= len(ls)
    avg[1] /= len(ls)
    dev = [0,0]
    for i in range(len(ls)):
        at = ls[i].split(" ")
        dev[0] += (float(at[0]) - avg[0]) ** 2
        dev[1] += (float(at[1]) - avg[1]) ** 2
    dev[0] /= len(ls) - 1
    dev[0] **= .5
    dev[1] /= len(ls) - 1
    dev[1] **= .5
    return avg[0], dev[0], avg[1], dev[1]


def readfile(n):
    f = "../matmult/det%d" % n
    fl = open(f)
    lines = fl.readlines()
    for i in range(int(len(lines) / 11)):
        ls = lines[11*i].split(" ")
        avg0, dev0, avg1, dev1 = getstat(lines[11*i+1:11*(i+1)])
        print(ls[2] + "," + repr(avg0) + "," + repr(dev0) + "," + repr(avg1) +
                "," + repr(dev1))

for i in range(4):
    print("N=" + repr(2**i))
    readfile(2 ** i)
    print()

