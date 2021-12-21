# 木の直径+1が答え
from collections import deque
INF = 10**9


def main():
    n = int(input())
    nei_of = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append(b)
        nei_of[b].append(a)

    st_node = 0
    far_node = st_node
    D = [INF]*n
    que = deque()
    que.append(st_node)
    D[st_node] = 0
    while que:
        pre = que.popleft()
        pre_d = D[pre]
        if D[far_node] < pre_d:
            far_node = pre
        d = pre_d + 1
        for cur in nei_of[pre]:
            if D[cur] <= d:
                continue
            D[cur] = d
            que.append(cur)

    st_node = far_node
    far_node = st_node
    D = [INF]*n
    que = deque()
    que.append(st_node)
    D[st_node] = 0
    while que:
        pre = que.popleft()
        pre_d = D[pre]
        if D[far_node] < pre_d:
            far_node = pre
        d = pre_d + 1
        for cur in nei_of[pre]:
            if D[cur] <= d:
                continue
            D[cur] = d
            que.append(cur)

    ans = D[far_node] + 1
    print(ans)


main()
