par = [i for i in range(10**5+1)]


def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]


def union(x, y):
    x = find(x)
    y = find(y)
    par[x] = y


def same(x, y):
    return find(x) == find(y)


def main():
    node_end, edge_end = map(int, input().split())
    node_end += 1
    edge_list = []
    for _ in range(edge_end):
        c, le, ri = map(int, input().split())
        le -= 1
        ri -= 1
        ri += 1
        edge_list.append((c, le, ri))
    edge_list.sort()

    ans = 0
    cnt = 0
    for c, a, b in edge_list:
        if same(a, b):
            continue
        ans += c
        cnt += 1
        union(a, b)

    if cnt == node_end-1:
        print(ans)
    else:
        print(-1)


main()
