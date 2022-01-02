from collections import deque


# 密グラフはスターグラフに
def main():
    node_end, group_end = map(int, input().split())
    group_list = []
    for _ in range(group_end):
        _ = input()
        group = list(map(lambda x: int(x)-1, input().split()))
        group_list.append(group)

    # 密グラフにした後のグラフをstared_graphと呼ぶことにする
    stared_node_end = node_end + group_end
    nei_of = [[] for _ in range(stared_node_end)]
    for stared_node, group in enumerate(group_list, node_end):
        # stared_node <-> groupに大してedgeを張る
        for node in group:
            nei_of[stared_node].append(node)
            nei_of[node].append(stared_node)

    # BFS
    que = deque()
    INF = float('inf')
    dist = [INF]*stared_node_end
    dist[0] = 0
    que.append(0)
    while que:
        pre = que.popleft()
        pre_d = dist[pre]
        cur_d = pre_d + 1
        for cur in nei_of[pre]:
            if dist[cur] > cur_d:
                dist[cur] = cur_d
                que.append(cur)

    for node in range(node_end):
        ans = dist[node]
        if ans == INF:
            ans = -1
        else:
            ans //= 2
        print(ans)


main()
