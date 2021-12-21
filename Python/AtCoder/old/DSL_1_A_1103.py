import sys
sys.setrecursionlimit(10**9)

# Union Find
par = [i for i in range(10**5+1)]


def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        par[x] = y


def same(x, y):
    return find(x) == find(y)


def main():
    n, q = map(int, input().split())
    ans = []
    for _ in range(q):
        c, x, y = map(int, input().split())
        if c == 0:
            union(x, y)
        else:
            is_same = same(x, y)
            if is_same:
                ans.append(1)
            else:
                ans.append(0)

    for a in ans:
        print(a)


main()
