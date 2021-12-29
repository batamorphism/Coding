# ダイクストラ
# from collections import deque
import queue
import heapq


def main():
    # input
    # n個のnode、m個のedge、
    # k個がゾンビに支配済み,s本が危険
    n, m, k, s = map(int, input().split())
    # 危険でない街ではp円、危険な街ではq円
    p, q = map(int, input().split())
    # ゾンビに支配済みの町
    zombie_node_list = [int(input())-1 for _ in range(k)]
    zombie_node_set = set(zombie_node_list)
    edge_dict = [[] for _ in range(n)]
    for _ in range(m):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        edge_dict[a].append(b)
        edge_dict[b].append(a)

    # 危険な街かを判定する
    # bfs
    danger_node = set()
    dist_danger = [10**10]*n
    que = queue.deque()
    for node in zombie_node_list:
        que.appendleft(node)
        dist_danger[node] = 0
    while que:
        current_node = que.popleft()
        if dist_danger[current_node] > s:  # 深さsで打ち止め
            break
        danger_node.add(current_node)
        neighbor_list = edge_dict[current_node]
        for neighbor in neighbor_list:
            if dist_danger[neighbor] <= dist_danger[current_node]+1:
                continue
            dist_danger[neighbor] = dist_danger[current_node]+1
            que.append(neighbor)

    # 最短距離を求める
    # ダイクストラ
    dist = [10**10]*n
    # distance, node からなる優先度付きqueue
    que = []

    dist[0] = 0
    heapq.heappush(que, [0, 0])

    # start dijkstra
    while que:
        d, current_node = heapq.heappop(que)
        if d > dist[current_node]:
            continue
        if current_node == n-1:
            que = []
            break
        for neighbor in edge_dict[current_node]:
            if neighbor == n-1:
                cost = 0
            elif neighbor in zombie_node_set:
                cost = 10**10
            elif neighbor in danger_node:
                cost = q
            else:
                cost = p
            if dist[neighbor] <= d+cost:
                continue
            dist[neighbor] = d+cost
            heapq.heappush(que, [dist[neighbor], neighbor])

    print(dist[-1])


main()
