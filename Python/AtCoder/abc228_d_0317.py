import sys
sys.setrecursionlimit(10**6)


def main():
    q = int(input())
    N = 2**20
    A = [-1]*N

    # setup union find
    par = [i for i in range(N)]

    def find(x):
        if x == par[x]:
            return x
        par[x] = find(par[x])
        return par[x]

    def union(lo, hi):
        lo = find(lo)
        hi = find(hi)
        if lo == hi:
            return
        par[lo] = hi

    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            h = x % N
            pos = find(h)
            A[pos] = x
            union(pos, (pos+1) % N)
        else:
            h = x % N
            print(A[h])


main()
