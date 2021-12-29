from collections import deque
import heapq as hp


def main():
    # input
    node_end, edge_end, zombie_node_end, danger_range = map(int, input().split())
    price_safe, price_danger = map(int, input().split())
    zombie_node_list = []
    for _ in range(zombie_node_end):
        c = int(input())
        c -= 1
        zombie_node_list.append(c)
    st_node = 0
    en_node = node_end-1
    super_zombie_node = node_end
    node_end += 1
    nei_of = [[] for _ in range(node_end)]
    for _ in range(edge_end):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append(b)
        nei_of[b].append(a)
    for zombie_node in zombie_node_list:
        nei_of[super_zombie_node].append(zombie_node)

    # BFS
    # 各zombie_nodeからの距離を求める
    INF = float('inf')
    dist = [INF] * node_end
    dist[super_zombie_node] = -1
    que = deque()
    que.append(super_zombie_node)
    while que:
        pre = que.popleft()
        pre_d = dist[pre]
        cur_d = pre_d + 1
        for cur in nei_of[pre]:
            if dist[cur] <= cur_d:
                continue
            dist[cur] = cur_d
            que.append(cur)

    # 各nodeの宿泊費を求める
    cost_of = [INF]*node_end
    for node in range(node_end):
        if node == en_node:
            cost = 0
        elif dist[node] == 0:
            cost = INF
        elif dist[node] <= danger_range:
            cost = price_danger
        elif dist[node] > danger_range:
            cost = price_safe
        cost_of[node] = cost

    # ダイクストラ
    que = []
    dist = [INF] * node_end
    dist[st_node] = 0
    hp.heappush(que, (0, st_node))
    while que:
        pre_d, pre_node = hp.heappop(que)
        if pre_d > dist[pre_node]:
            continue
        for cur_node in nei_of[pre_node]:
            cur_d = pre_d + cost_of[cur_node]
            if dist[cur_node] <= cur_d:
                continue
            dist[cur_node] = cur_d
            hp.heappush(que, (cur_d, cur_node))

    ans = dist[en_node]
    print(ans)


main()
