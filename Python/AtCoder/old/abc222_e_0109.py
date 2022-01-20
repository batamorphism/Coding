from collections import deque
MOD = 998244353
INF = float('inf')
import pprint


# a_i -> a_i+1の最短経路を求める
# O(N^2)で間に合う
# それぞれ、各辺を通った回数を数える
# その後ナップザックDP
def main():
    node_end, a_end, k = map(int, input().split())
    edge_end = node_end - 1
    A = list(map(lambda x: int(x) - 1, input().split()))
    nei_of = [[] for _ in range(node_end)]
    for i in range(node_end - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        nei_of[u].append((v, i))
        nei_of[v].append((u, i))

    cnt_of = [0]*edge_end
    # a_i -> a_jのbfsを繰り返す
    for i, a_i in enumerate(A[:-1]):
        j = i + 1
        a_j = A[j]
        dist = [INF]*node_end
        dist[a_i] = 0
        par_of = [None for _ in range(node_end)]
        que = deque()
        que.append(a_i)
        while que:
            pre = que.popleft()
            pre_d = dist[pre]
            cur_d = pre_d + 1
            for cur, edge_id in nei_of[pre]:
                if dist[cur] <= cur_d:
                    continue
                dist[cur] = cur_d
                par_of[cur] = (pre, edge_id)
                que.append(cur)
        cur = a_j
        while par_of[cur]:
            cur, edge_id = par_of[cur]
            cnt_of[edge_id] += 1

    # print(cnt_of)
    # c = R+Bとする
    # R-B=K ->両辺に+cする
    # 2*R = k+c
    c = sum(cnt_of)
    k += c
    if k % 2 == 1:
        print(0)
        return
    if k < 0:
        print(0)
        return
    k //= 2
    # R = kとなるRの選び方
    # cnt_ofからいくつか選び、合計がkとなるようにする
    # DP[i][val] := i番目までのRの選び方のうち、合計がvalとなるものの個数
    DP = [[0]*(k+1) for _ in range(edge_end+1)]
    # 1-indexed
    DP[0][0] = 1
    for i in range(1, edge_end+1):
        for val in range(k+1):
            dp = DP[i-1][val]  # 選ばない場合
            if val - cnt_of[i-1] >= 0:
                dp += DP[i-1][val-cnt_of[i-1]]
            dp %= MOD
            DP[i][val] = dp

    ans = DP[edge_end][k]
    print(ans)


main()
