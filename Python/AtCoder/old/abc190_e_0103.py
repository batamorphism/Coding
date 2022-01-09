# 互いの石同士の距離を求める
# そのあと、巡回セールスマン
from collections import deque
INF = float('inf')


def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    for _ in range(edge_end):
        a, b = map(lambda x: int(x) - 1, input().split())
        nei_of[a].append(b)
        nei_of[b].append(a)
    k = int(input())
    C = list(map(lambda x: int(x)-1, input().split()))

    dist = [[INF]*k for _ in range(k)]
    for i, fr in enumerate(C):
        dist_fr = [INF]*node_end
        que = deque([fr])
        dist_fr[fr] = 0
        while que:
            pre = que.popleft()
            pre_d = dist_fr[pre]
            cur_d = pre_d + 1
            for cur in nei_of[pre]:
                if dist_fr[cur] > cur_d:
                    dist_fr[cur] = cur_d
                    que.append(cur)
        for j, to in enumerate(C):
            dist[i][j] = dist_fr[to]

    """
    for d in dist:
        print(d)
    """
    # どういう経路でCをたどっていけば、距離が最小となるか
    # S:= 既に訪れた石、i := 最後に訪れた石 の状態にするのに必要な距離
    ALL = 1 << k
    DP = [[INF] * k for _ in range(ALL)]
    for i in range(k):
        DP[1 << i][i] = 1
    for S in range(ALL):
        for i in range(k):
            if not (S >> i) & 1:
                continue
            pre_S = S ^ (1 << i)
            dp = DP[S][i]
            for j in range(k):
                # j -> i に移動することで遷移する
                if not (pre_S >> j) & 1:
                    continue
                dp = min(dp, DP[pre_S][j] + dist[j][i])
            DP[S][i] = dp

    ans = min(DP[ALL-1])
    if ans == INF:
        ans = -1
    print(ans)


main()
