import sys
sys.setrecursionlimit(10**6)


node_end, m = map(int, input().split())
D = list(map(int, input().split()))
edge_list = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(m)]

# setup union find
par = [i for i in range(node_end)]
siz = [1]*node_end

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
    # siz[x] <= siz[y]
    if not siz[x] <= siz[y]:
        x, y = y, x
    par[x] = y
    siz[y] += siz[x]

def is_same(x, y):
    return find(x) == find(y)

if sum(D) != 2*(node_end-1):
    print(-1)
    exit()

for a, b in edge_list:
    if is_same(a, b):
        print(-1)
        exit()
    union(a, b)
    D[a] -= 1
    D[b] -= 1
    if D[a] < 0 or D[b] < 0:
        print(-1)
        exit()

# 各連結成分ごとに使えるnode
useful_of = [[] for _ in range(node_end)]
for node in range(node_end):
    par_node = find(node)
    for _ in range(D[node]):
        useful_of[par_node].append(node)

# 使えるノードが2つ以上ある場合は、large
# 使えるノードが1つの場合は、small
large_list = []
small_list = []
for node in range(node_end):
    useful = useful_of[node]
    if len(useful) >= 2:
        large_list.append(node)
    elif len(useful) == 1:
        small_list.append(node)
    # 代表元以外は、len==0である

# 貪欲法でグラフを構築
ans_list = []
while large_list and small_list:
    fr = large_list.pop()
    to = small_list.pop()
    fr_useful = useful_of[fr]
    to_useful = useful_of[to]
    use1 = fr_useful.pop()
    use2 = to_useful.pop()
    ans_list.append((use1+1, use2+1))

    # len(to_useful) == 0なので死にロジック
    union(to, fr)
    if len(fr_useful) == 1:
        small_list.append(fr)
    else:
        large_list.append(fr)

if large_list:
    print(-1)
    exit()
if len(small_list) != 2:
    print(-1)
    exit()

fr = small_list.pop()
to = small_list.pop()
fr_useful = useful_of[fr]
to_useful = useful_of[to]
use1 = fr_useful.pop()
use2 = to_useful.pop()
ans_list.append((use1+1, use2+1))

for ans in ans_list:
    print(*ans)
