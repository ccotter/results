#!/usr/bin/python

# To format pqsort evals into CSV format (pthreads and deterministic).

def readfile(n, s):
    f = "../pqsort/%s%d" % (s, n)
    fl = open(f)
    lines = fl.readlines()
    print("N=%d" % n)
    for i in range(1, int(len(lines))):
        l = lines[i].split(" ")
        sz = int(l[1].split("\t")[0])
        t = float(l[3])
        print("%d,%f" % (sz, t))
    print()

for i in range(4):
        readfile(2 ** i, "pthread")
for i in range(4):
        readfile(2 ** i, "det")

