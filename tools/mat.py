#!/usr/bin/python

# To format pthread matmult evals into CSV format.

def readfile(n):
    f = "../matmult/pthread%d" % n
    fl = open(f)
    lines = fl.readlines()
    print("N=%d" % n)
    for i in range(int(len(lines) / 2)):
        sz = lines[2*i].split(" ")[2]
        t = float(lines[2*i+1].split(":")[1])
        print("%s,%f" % (sz,t))
    print()

for i in range(4):
        readfile(2 ** i)

