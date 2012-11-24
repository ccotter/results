#!/usr/bin/python

# To format md5 evals into CSV format (pthread, deterministic).

def readfile(n, s):
    f = "../md5/%s%d" % (s, n)
    fl = open(f)
    lines = fl.readlines()
    print("N=%d" % n)
    total = 0
    for i in range(int(len(lines) / 3)):
        total += float(lines[3*i+1].split(" ")[9])
    print(total / (len(lines)/3))

for i in range(4):
        readfile(2 ** i, "pthread")
for i in range(4):
        readfile(2 ** i, "det")

