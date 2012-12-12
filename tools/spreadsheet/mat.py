#!/usr/bin/python

# To format pthread matmult evals into CSV format.

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
    f = "../../matmult/pthread%d" % n
    fl = open(f)
    lines = fl.readlines()
    for i in range(int(len(lines) / 11)):
        ls = lines[11*i].split(" ")
        avg, dev = getstat(lines[11*i+1:11*(i+1)])
        print(ls[2] + "," + repr(avg) + "," + repr(dev))

for i in range(4):
    print("N=" + repr(2**i))
    readfile(2 ** i)
    print()

