import sys
sys.setrecursionlimit(10**9)

par = [i for i in range(10**5*2 + 1)]

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


def is_same(x, y):
    return find(x) == find(y)


def main():
    node_end, edge_end = map(int, input().split())
    edge_list = []
    for _ in range(edge_end):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        edge_list.append((c, a, b))

    edge_list.sort()
    ans = 0
    for c, a, b in edge_list:
        if c <= 0:
            # 罰金を払うやつは常に取り除かない
            union(a, b)
        else:
            if not is_same(a, b):
                # 取り除いてはならない
                union(a, b)
            else:
                ans += c

    print(ans)


main()
