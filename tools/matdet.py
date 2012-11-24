#!/usr/bin/python

# To format deterministic matmult evals into CSV format.

def readfile(n):
    f = "../matmult/det%d" % n
    fl = open(f)
    lines = fl.readlines()
    print("N=%d" % n)
    for i in range(int(len(lines) / 3)):
        sz = lines[3*i].split(" ")[2]
        t = float(lines[3*i+1].split(":")[1])
        tm = float(lines[3*i+2].split(":")[1])
        print("%s,%f,%f" % (sz,t,tm))
    print()

for i in range(4):
        readfile(2 ** i)

