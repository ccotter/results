#!/usr/bin/python

# To format pqsort evals into CSV format.

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


def readfile(s, n):
    f = "../pqsort/%s%d" % (s, n)
    fl = open(f)
    lines = fl.readlines()
    for i in range(int(len(lines) / 11)):
        ls = lines[11*i].split(" ")
        avg, dev = getstat(lines[11*i+1:11*(i+1)])
        print(ls[1][:-2] + "," + repr(avg) + "," + repr(dev))

for i in range(4):
    print("N=" + repr(2**i))
    readfile("pthread", 2 ** i)
    print()
for i in range(4):
    print("N=" + repr(2**i))
    readfile("det", 2 ** i)
    print()

