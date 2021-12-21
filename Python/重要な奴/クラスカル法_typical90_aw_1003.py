# UnionFind
parent = [i for i in range(10**5+1)]

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    parent[a] = b

def same(a, b):
    return find(a) == find(b)


def main():
    # 各ビット列bに対し、[0]+b+[0]を考え
    # dを、b[i]==b[i+1]を表すビット列とする
    # b=_111000_の場合、
    # d=1001000_ となる
    # これは、L~Rを反転させる操作を
    # LとR+1に1を挿入する操作に変換する

    # dのすべての組み合わせ2**(n+1)のうち、偶数個の1がある2**nがすべて実現できればよい
    # LとR+1を結ぶedgeを考え、これの最小全域木を考えればよい

    n, m = map(int, input().split())
    n_end = n+1
    edge_list = []
    for _ in range(m):
        cost, left, right = map(int, input().split())
        # 0-indexedなので1引いたあと、right++
        edge_list.append((cost, left-1, right))

    # kruskal
    edge_list.sort()
    ans = 0
    for edge in edge_list:
        co, fr, to = edge
        if not same(fr, to):
            union(fr, to)
            ans += co

    # 連結になっているか確認
    for n in range(n_end):
        if not same(0, n):
            print(-1)
            return

    print(ans)


main()
