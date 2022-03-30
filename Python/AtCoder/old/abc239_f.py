import heapq
import sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)
# 最小全域木？
# dが大きい奴からクラスカル


def main():
    node_end, m = map(int, input().split())
    D = list(map(int, input().split()))
    d_of = [0] * node_end
    for node, d_node in enumerate(D):
        d_of[node] = d_node

    del D

    # union find
    par = [i for i in range(node_end)]
    d_tot = d_of[:]
    remain_node = [[] for _ in range(node_end)]  # dが1以上残っているもの
    for node in range(node_end):
        d = d_of[node]
        if d >= 1:
            remain_node[node].append(node)

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
        d_tot[y] += d_tot[x] - 2
        rem_x = remain_node[x][-1]
        rem_y = remain_node[y][-1]
        d_of[rem_x] -= 1
        d_of[rem_y] -= 1
        if d_of[rem_x] == 0:
            remain_node[x].pop()
        if d_of[rem_y] == 0:
            remain_node[y].pop()
        remain_node[y] += remain_node[x]
        return (rem_x, rem_y)

    def is_same(x, y):
        return find(x) == find(y)

    def get_d(x):
        return d_tot[find(x)]

    def get_all():
        done = set()
        for node in range(node_end):
            x = find(node)
            if x not in done:
                done.add(x)
                yield x

    for _ in range(m):
        a, b = map(lambda x: int(x)-1, input().split())
        if is_same(a, b):
            print(-1)
            return
        union(a, b)

    # d_totが大きい順に、くっつけていく
    que = []
    for node in get_all():
        d = get_d(node)
        que.append((-d, node))

    ans_list = []

    while que:
        d_fr, fr = heapq.heappop(que)
        if d_fr == 0:
            print(-1)
            return
        if not que:
            print(-1)
            return
        d_to, to = heapq.heappop(que)
        if d_to == 0:
            print(-1)
            return
        d_fr *= -1
        d_to *= -1
        # frとtoをくっつける
        rem_fr, rem_to = union(fr, to)
        ans_list.append((rem_fr+1, rem_to+1))
        # yが親になる
        fr = find(fr)
        d_fr = get_d(fr)
        if d_fr != 0:
            heapq.heappush(que, (-d_fr, fr))

    # print(d_of)

    for fr, to in ans_list:
        print(fr, to)


main()
