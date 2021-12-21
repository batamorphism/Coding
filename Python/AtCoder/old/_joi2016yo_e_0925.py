from collections import deque
import heapq as hq
from collections import namedtuple


def main():
    # STEP1:BFSで各町の宿泊費を計算する
    # zombie_node = INF
    # danger_node = q
    # safe_node = p
    # goal_node = 0
    # ここで、super_zombie_nodeを作成し、zombie_nodeへのedgeを張る
    # STEP2:Dijkstraで最短コストを計算する

    # input
    # n:nodes
    # m:edges
    # k:zombie
    # s:danger_distance
    INF = 10**10
    n, m, k, s = map(int, input().split())
    p, q = map(int, input().split())
    zombie_node_list = []
    for _ in range(k):
        zombie_node_list.append(int(input())-1)
    edge_list = []
    for _ in range(m):
        a, b = map(int, input().split())
        edge_list.append([a-1, b-1])

    super_zombie_node = n
    for zombie_node in zombie_node_list:
        edge_list.append([super_zombie_node, zombie_node])

    neighbor_of = [[] for _ in range(n+1)]
    for edge in edge_list:
        a, b = edge
        neighbor_of[a].append(b)
        neighbor_of[b].append(a)

    # BFS
    # calc_costs
    cost_of = [INF]*(n+1)
    dist_bfs = [INF]*(n+1)
    que = deque()
    dist_bfs[super_zombie_node] = -1
    que.append(super_zombie_node)
    while que:
        pre_node = que.popleft()
        if dist_bfs[pre_node] > s:
            break
        for cur_node in neighbor_of[pre_node]:
            # 打ち切り処理
            if dist_bfs[cur_node] <= dist_bfs[pre_node]+1:
                continue
            dist_bfs[cur_node] = dist_bfs[pre_node]+1
            que.append(cur_node)

    for node in range(n+1):
        if dist_bfs[node] <= 0:
            cost_of[node] = INF
        elif node == n-1:
            cost_of[node] = 0
        elif dist_bfs[node] <= s:
            cost_of[node] = q
        else:
            cost_of[node] = p

    # dijkstra
    que = []
    dist = [INF]*(n+1)
    Node = namedtuple('Dijkstra_node', ['dist', 'node'])
    s_node_tup = Node(dist=0, node=0)
    hq.heappush(que, s_node_tup)
    dist[0] = 0
    while que:
        pre_node_tup = hq.heappop(que)
        # 打ち切り処理
        if pre_node_tup.dist > dist[pre_node_tup.node]:
            continue
        # 停止処理
        if pre_node_tup.node == n-1:
            ans = pre_node_tup.dist
        for cur_node in neighbor_of[pre_node_tup.node]:
            cost = cost_of[cur_node]
            cur_node_tup = Node(dist=pre_node_tup.dist+cost, node=cur_node)
            if cur_node_tup.dist >= dist[cur_node_tup.node]:
                continue
            dist[cur_node_tup.node] = cur_node_tup.dist
            hq.heappush(que, cur_node_tup)

    print(ans)


main()
