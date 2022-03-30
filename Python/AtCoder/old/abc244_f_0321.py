from collections import deque


# 状態を、Sと今いる頂点vからなる(S, v)で定義する
def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    for _ in range(edge_end):
        fr, to = map(lambda x: int(x)-1, input().split())
        nei_of[fr].append(to)
        nei_of[to].append(fr)

    # bitDP+BFS
    ALL = 1 << node_end
    INF = float('inf')
    DP = [[INF]*node_end for _ in range(ALL)]
    que = deque()

    # 初期化
    for node in range(node_end):
        S = 1 << node
        que.append((S, node))
        DP[S][node] = 1

    # BFS
    while que:
        pre_S, pre_node = que.popleft()
        cur_d = DP[pre_S][pre_node]+1
        for cur_node in nei_of[pre_node]:
            cur_S = pre_S ^ (1 << cur_node)  # cur_nodeに偶数回来たかをxorで処理
            if DP[cur_S][cur_node] <= cur_d:
                continue
            DP[cur_S][cur_node] = cur_d
            que.append((cur_S, cur_node))

    # 0, 0の時の特殊処理
    DP[0][0] = 0
    ans = 0
    for S in range(ALL):
        pre_ans = INF
        for node in range(node_end):
            pre_ans = min(pre_ans, DP[S][node])
        ans += pre_ans
    print(ans)


main()
