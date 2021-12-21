from collections import deque
INF = 10**6


def main():
    n = int(input())
    nei_of = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append(b)
        nei_of[b].append(a)

    # BFSでst_nodeからの距離を計測する
    dist = [INF]*n
    st_node = 0
    dist[st_node] = 0
    que = deque([st_node])
    while que:
        pre = que.popleft()
        d = dist[pre]
        d += 1
        for cur in nei_of[pre]:
            if dist[cur] <= d:
                continue
            dist[cur] = d
            que.append(cur)

    # 距離が偶数の者と奇数のものをピックアップする
    odd = []
    eve = []
    for node in range(n):
        if dist[node] % 2 == 0:
            eve.append(node)
        else:
            odd.append(node)

    if len(eve) > len(odd):
        ans = eve[:n//2]
    else:
        ans = odd[:n//2]

    ans = [a+1 for a in ans]
    print(*ans)


main()
