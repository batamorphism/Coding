# 距離が偶数か奇数か
from collections import deque


def main():
    node_end, query_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    for _ in range(node_end-1):
        fr, to = map(lambda x: int(x)-1, input().split())
        nei_of[fr].append(to)
        nei_of[to].append(fr)

    INF = float('inf')
    dist = [INF]*node_end
    dist[0] = 0
    que = deque([0])
    while que:
        pre = que.popleft()
        pre_d = dist[pre]
        cur_d = pre_d + 1
        for cur in nei_of[pre]:
            if dist[cur] <= cur_d:
                continue
            dist[cur] = cur_d
            que.append(cur)

    ans_list = []
    for _ in range(query_end):
        c, d = map(lambda x: int(x)-1, input().split())
        diff = abs(dist[c]-dist[d])
        if diff % 2 == 0:
            ans = 'Town'
        else:
            ans = 'Road'
        ans_list.append(ans)

    print(*ans_list, sep='\n')


main()
