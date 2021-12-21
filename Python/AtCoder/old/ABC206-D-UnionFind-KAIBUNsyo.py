import networkx as x

# *a:可変長位置変数、第2引数以降をタプル型で受け取る
n, *a = map(int, open(0).read().split())
G = x.Graph()
u = x.utils.union_find.UnionFind()

# //:切り捨て除算

for i in range(n//2):
    if a[i] != a[n-i-1]:    # a[i]とa[n-i-1]が異なっていたら、同じグループに入れる
        u.union(a[i], a[n-i-1])


#u[i]: グラフの要素iに対し、親が何かを返す
trees = [u[i] for i in a]

print(len(set(a))-len(set(trees)))
