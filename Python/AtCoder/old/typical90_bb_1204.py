from collections import deque
INF = float('inf')


def main():
    n, m = map(int, input().split())
    node_end = n
    nei_of = [set() for _ in range(n)]
    for _ in range(m):
        _ = int(input())
        R = list(map(int, input().split()))
        R = [r-1 for r in R]
        # 新しくnodeを追加し、そいつとRを繋ぐ
        # スターハブ状にする
        r_node = node_end
        node_end += 1
        nei_of.append(set())
        for r in R:
            nei_of[r_node].add(r)
            nei_of[r].add(r_node)

    dist = [INF]*node_end
    dist[0] = 0  # 高橋君の距離は0
    que = deque()
    que.append(0)
    while que:
        pre = que.popleft()
        pre_d = dist[pre]
        d = pre_d + 1
        for cur in nei_of[pre]:
            if dist[cur] <= d:
                continue
            dist[cur] = d
            que.append(cur)

    for i in range(n):
        ans = dist[i]
        if ans > n*2:
            ans = -1
        else:
            ans //= 2
        print(ans)


main()
