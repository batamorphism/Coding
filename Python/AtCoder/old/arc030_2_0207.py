# 経路圧縮+BFS
from collections import deque


def main():
    node_end, x = map(int, input().split())
    x -= 1
    visit_node = list(map(int, input().split()))
    visit_node[x] = 1
    nei_of = [[] for _ in range(node_end)]
    for _ in range(node_end-1):
        a, b = map(lambda x: int(x)-1, input().split())
        nei_of[a].append(b)
        nei_of[b].append(a)

    # DFSでの訪問順に、最短経路を計算していく
    order = [-1]*node_end
    que = deque([x])
    order[x] = 0
    cur_order = 0
    while que:
        pre = que.popleft()
        order[pre] = cur_order
        cur_order += 1
        for cur in nei_of[pre]:
            if order[cur] != -1:
                continue
            que.appendleft(cur)

    ans = 0
    INF = float('inf')
    node_list = [i for i in range(node_end) if visit_node[i] == 1]
    node_list.sort(key=lambda x: order[x])
    if node_list[0] != x:
        raise
    node_list.append(node_list[0])
    for i, fr in enumerate(node_list[:-1]):
        to = node_list[i+1]
        dist = [INF]*node_end
        dist[fr] = 0
        que = deque([fr])
        while que:
            pre = que.popleft()
            cur_d = dist[pre] + 1
            for cur in nei_of[pre]:
                if dist[cur] <= cur_d:
                    continue
                dist[cur] = cur_d
                que.append(cur)
        ans += dist[to]

    print(ans)


main()
