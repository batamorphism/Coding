# State = (S, 最後の頂点)
from collections import deque


def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    for _ in range(edge_end):
        fr, to = map(lambda x: int(x) - 1, input().split())
        nei_of[fr].append(to)
        nei_of[to].append(fr)

    # BFS
    INF = float('inf')
    ALL = 1 << node_end
    # dist[S][node]
    dist = [[INF]*node_end for _ in range(ALL)]
    que = deque()

    # 初期化
    for node in range(node_end):
        dist[1 << node][node] = 1
        que.append((1 << node, node))

    while que:
        pre_S, pre_node = que.popleft()
        pre_d = dist[pre_S][pre_node]
        cur_d = pre_d + 1
        for cur_node in nei_of[pre_node]:
            cur_S = pre_S ^ (1 << cur_node)
            if dist[cur_S][cur_node] <= cur_d:
                continue
            dist[cur_S][cur_node] = cur_d
            que.append((cur_S, cur_node))

    # Sが0のとき、nodeをうまく定義できないので、ここで特殊処理
    dist[0][0] = 0

    ans = 0
    for S in range(ALL):
        pre_ans = INF
        for node in range(node_end):
            pre_ans = min(pre_ans, dist[S][node])
        ans += pre_ans
    print(ans)


main()
