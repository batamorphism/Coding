from numba import njit
import sys
import numpy
import random
import time
import copy
from itertools import product
INF = float('inf')

print(sys.argv[-1])

def main():
    node_end = 100
    adj = numpy.array([numpy.array([0] * node_end, dtype=numpy.int64) for _ in range(node_end)], dtype=numpy.int64)
    for fr, to in product(range(node_end), repeat=2):
        adj[fr][to] = random.randint(1, 100)

    st_time = time.perf_counter()
    for _ in range(10):
        dist = copy.deepcopy(adj)
        wf(node_end, dist)
    en_time = time.perf_counter()
    print(en_time - st_time)



# @njit
@njit('i8(i8,i8[:,:])', cache=True)
def wf(node_end, adj):
    # dist = [[INF]*node_end for _ in range(node_end)]
    dist = adj
    for fr in range(node_end):
        for to in range(node_end):
            dist[fr][to] = adj[fr][to]
    # for k, fr, to in itertools.product(range(node_end), repeat=3):
    for k in range(node_end):
        for fr in range(node_end):
            for to in range(node_end):
                d1 = dist[fr][to]
                d2 = dist[to][k] + dist[k][to]
                dist[fr][to] = min(d1, d2)

    return dist[0][node_end-1]


def cc_export():
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('solve', '(i8[:],)')(solve)
    cc.compile()

if __name__ == '__main__':
    import sys
    if sys.argv[-1] == 'ONLINE_JUDGE':
        cc_export()
        exit(0)
    from my_module import solve
    main()
