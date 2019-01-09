from euler.algorithms.ds import DisjointSet
from operator import itemgetter

def min_span_tree(nodes, edges):
    forest = DisjointSet()
    mst = []
    for n in nodes:
        forest.add(n)
    sz = len(nodes) - 1
    for e in sorted( edges, key=itemgetter(2)):
        n1, n2, _ = e
        t1 = forest.find(n1)
        t2 = forest.find(n2)
        if t1 != t2:
            mst.append(e)
            sz -= 1
            if sz == 0:
                return mst
            forest.union(t1, t2)