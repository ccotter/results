#!/usr/bin/python

# To format md5 evals into CSV format (pthread, deterministic).

def getstat(ls):
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

def add(r, a, b):
    v = r.get(a)
    if v is None:
        v = r[a] = []
    v.append(b)

def dogroup(n, s):
    results = {}
    for i in range(5):
        f = "../../md5/%s%d-%d" % (s, n, (i+1))
        fl = open(f)
        lines = fl.readlines()
        for j in range(int(len(lines) / 3)):
            at = lines[3*j + 1].split(" ")
            add(results, at[7][0:4], at[9])
    tot = []
    for i in range(5):
        tmp = []
        for a in results:
            tmp.append(results[a][i])
        avg, dev = getstat(tmp)
        tot.append(avg)
    avg, dev = getstat(tot)
    print(repr(avg) + "," + repr(dev))

for i in range(4):
    dogroup(2 ** i, "pthread")
for i in range(4):
    dogroup(2 ** i, "det")

