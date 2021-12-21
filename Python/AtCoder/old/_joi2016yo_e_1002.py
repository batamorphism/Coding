from collections import deque as deq
import heapq as hq


def main():
    INF = 10**10

    node_end, edge_end, zombie_end, danger_range = map(int, input().split())
    safe_price, danger_price = map(int, input().split())
    node_goal = node_end-1
    zombie_list = []
    for _ in range(zombie_end):
        zombie_list.append(int(input())-1)
    edge_list = []
    for _ in range(edge_end):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        edge_list.append((a, b))
    nei_of = [[] for _ in range(node_end+10)]
    for edge in edge_list:
        nei_of[edge[0]].append(edge[1])
        nei_of[edge[1]].append(edge[0])

    # zombie_listから距離danger_rangeのnodeを判定する
    node_end += 1
    super_zombie_node = node_end-1
    for zombie_node in zombie_list:
        nei_of[super_zombie_node].append(zombie_node)
    # BFS
    dist_bfs = [INF]*node_end
    que = deq()
    dist_bfs[super_zombie_node] = -1
    que.append(super_zombie_node)
    while que:
        pre_node = que.popleft()
        for cur_node in nei_of[pre_node]:
            d = dist_bfs[pre_node] + 1
            if dist_bfs[cur_node] <= d:
                continue
            dist_bfs[cur_node] = d
            que.append(cur_node)

    # calc costs
    cost_of = [INF]*node_end
    set_zombie_list = set(zombie_list)
    for node in range(node_end):
        if node == super_zombie_node:
            cost_of[node] = INF
        elif node == node_goal:
            cost_of[node] = 0
        elif node in set_zombie_list:
            cost_of[node] = INF
        elif dist_bfs[node] <= danger_range:
            cost_of[node] = danger_price
        else:
            cost_of[node] = safe_price

    # dijkstra
    que = []
    dist = [INF]*node_end
    dist[0] = 0
    # node = (dist, node)
    hq.heappush(que, (0, 0))
    while que:
        pre_dist, pre_node = hq.heappop(que)
        if pre_dist > dist[pre_node]:  # 打ち切り
            continue
        if pre_node == node_goal:  # 停止処理
            break
        for cur_node in nei_of[pre_node]:
            d = pre_dist + cost_of[cur_node]
            if dist[cur_node] <= d:
                continue
            dist[cur_node] = d
            hq.heappush(que, (d, cur_node))

    print(dist[node_goal])


main()
