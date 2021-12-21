import sys
sys.setrecursionlimit(10**6)


def main():
    n, m = map(int, input().split())

    edge_list = []
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edge_list.append((a, b))

    # Setup Union Find
    par = [i for i in range(n)]
    siz = [1]*n

    def find(x):
        if x == par[x]:
            return x
        par[x] = find(par[x])
        return par[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        par[x] = y
        siz[y] += siz[x]
        return

    def get_size(x):
        x = find(x)
        return siz[x]

    ans_list = []
    ans = 0
    for edge in reversed(edge_list):
        ans_list.append(ans)
        a, b = edge
        if find(a) != find(b):
            # print(a+1, b+1, siz[a], siz[b])
            ans += get_size(a)*get_size(b)  # 新たに通れるようになった島の組み合わせ数
            union(a, b)

    # print(ans_list)
    total = n*(n-1)//2
    for ans in reversed(ans_list):
        print(total-ans)


main()
