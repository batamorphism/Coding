from collections import deque
INF = float('inf')
MOD = 998244353


# m回の操作それぞれについて、最短経路をBFSで求める
# ->O(m*n) -> O(100000) 間に合う
# 最短経路で、それぞれの辺を何回通ったかカウントする
# R-B = K, 最短経路の総数をCとすると、R+B = Cであり
# 2R = K + C
# K + Cが奇数なら0
# K + C // 2をXとして
# いくつか辺を選んで、合計がXとなるようにすればよい。ナップザック問題
def main():
    node_end, m, k = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]
    nei_of = [[] for _ in range(node_end)]
    for i in range(node_end-1):
        fr, to = map(int, input().split())
        fr -= 1
        to -= 1
        nei_of[fr].append((to, i))
        nei_of[to].append((fr, i))

    # 各辺を最短経路で何回通るか
    cnt_of = [0] * (node_end-1)
    for st_i in range(m-1):
        en_i = st_i+1
        st = A[st_i]
        en = A[en_i]
        path = get_path(nei_of, node_end, st, en)
        for edge_id in path:
            cnt_of[edge_id] += 1

    # print(cnt_of)

    c = sum(cnt_of)
    if (k + c) % 2 == 1:
        print(0)
        return

    k = (k+c)//2

    if k < 0:
        print(0)
        return

    # cnt_ofからいくつか選んで、合計をkにする
    # DP[val] = 合計がvalとなる組み合わせ数
    # O(1000*10000)
    DP = [0] * (k+1)
    DP[0] = 1
    # 配るDP
    for cnt in cnt_of:
        new_DP = [0] * (k+1)
        for cur_val in range(k+1):
            # cntを足さない
            new_DP[cur_val] += DP[cur_val]
            # cntを足す
            nex_val = cur_val + cnt
            if nex_val > k:
                continue
            new_DP[nex_val] += DP[cur_val]
        for val in range(k+1):
            DP[val] = new_DP[val] % MOD

    print(DP[k])


def get_path(nei_of, node_end, st, en):
    # st -> enの最短経路のパスを求める
    dist = [INF] * node_end
    par_of = {}  # par_of[cur] = (pre, edge_id)
    que = deque()
    que.append(st)
    dist[st] = 0
    while que:
        pre = que.popleft()
        pre_d = dist[pre]
        cur_d = pre_d + 1
        for cur, edge_id in nei_of[pre]:
            if dist[cur] > cur_d:
                dist[cur] = cur_d
                que.append(cur)
                par_of[cur] = (pre, edge_id)

    ret = []
    cur = en
    while cur != st:
        par = par_of[cur]
        ret.append(par[1])
        cur = par[0]
    return ret[::-1]


main()
