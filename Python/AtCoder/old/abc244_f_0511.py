from collections import deque

def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    for _ in range(edge_end):
        fr, to = map(int, input().split())
        fr -= 1
        to -= 1
        nei_of[fr].append(to)
        nei_of[to].append(fr)

    # DP[S][node]: S, nodeに関する最小の長さ
    # S: 各頂点を通った回数の偶奇
    # node: 現在いる頂点
    INF = float('inf')
    S_end = 1 << node_end
    DP = [[INF]*node_end for _ in range(S_end)]

    # 初期値+que
    que = deque()
    for node in range(node_end):
        cur_S = 1 << node
        que.append((cur_S, node))
        DP[cur_S][node] = 1

    # 配るDP
    while que:
        pre_S, pre_node = que.popleft()
        pre_d = DP[pre_S][pre_node]
        cur_d = pre_d + 1
        for cur_node in nei_of[pre_node]:
            cur_S = pre_S ^ (1 << cur_node)
            if DP[cur_S][cur_node] > cur_d:
                DP[cur_S][cur_node] = cur_d
                que.append((cur_S, cur_node))

    # 0の処理
    DP[0][0] = 0

    ans = 0
    for cur_S in range(S_end):
        ans += min(DP[cur_S])

    print(ans)


main()
