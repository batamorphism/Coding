from collections import deque
import heapq as hq
INF = 10**10+1


def main():
    n_end, m, k, s = map(int, input().split())
    to_node = n_end - 1
    fr_node = 0
    super_node = n_end
    n_end += 1  # SUPER NODE分追加
    safe_cost, dang_cost = map(int, input().split())
    nei_of = [[] for _ in range(n_end)]
    for _ in range(k):
        c = int(input())
        c -= 1
        nei_of[super_node].append(c)
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append(b)
        nei_of[b].append(a)

    # BFSで各町の宿泊費を決定する
    dist = [INF]*n_end
    que = deque()
    que.append(super_node)
    dist[super_node] = -1
    while que:
        pre_node = que.popleft()
        d = dist[pre_node]
        d += 1
        for cur_node in nei_of[pre_node]:
            if dist[cur_node] <= d:
                continue
            dist[cur_node] = d
            que.append(cur_node)

    cost_of = [0]*n_end
    for node in range(n_end):
        if node == to_node:
            cost_of[node] = 0
        elif dist[node] == -1:
            cost_of[node] = INF
        elif dist[node] == 0:
            cost_of[node] = INF
        elif dist[node] <= s:
            cost_of[node] = dang_cost
        else:
            cost_of[node] = safe_cost

    # ダイクストラ
    cost = [INF]*n_end
    que = []
    hq.heappush(que, (0, fr_node))
    cost[fr_node] = 0
    while que:
        pre_cost, pre_node = hq.heappop(que)
        c = cost[pre_node]
        if pre_cost > c:  # 打ち切り
            continue
        for cur_node in nei_of[pre_node]:
            cur_cost = c + cost_of[cur_node]
            if cur_cost >= cost[cur_node]:
                continue
            cost[cur_node] = cur_cost
            hq.heappush(que, (cur_cost, cur_node))
    print(cost[to_node])


main()
