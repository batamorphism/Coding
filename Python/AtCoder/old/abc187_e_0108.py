from collections import deque


# 処理する順番には依存しない
# 木は辺
# rootにx_iを足し、b_eにx_iを引く
def main():
    n = int(input())
    nei_of = [[] for _ in range(n)]
    edge_list = []
    for _ in range(n-1):
        a, b = map(lambda x: int(x) - 1 , input().split())
        nei_of[a].append(b)
        nei_of[b].append(a)
        edge_list.append((a, b))

    # 各頂点の、rootからの距離を求める
    INF = float('inf')
    dist = [INF]*n
    root = 0
    dist[root] = 0
    que = deque()
    que.append(root)
    while que:
        pre = que.popleft()
        pre_d = dist[pre]
        cur_d = pre_d + 1
        for cur in nei_of[pre]:
            if dist[cur] <= cur_d:
                continue
            dist[cur] = cur_d
            que.append(cur)

    C = [0]*n
    q = int(input())
    for _ in range(q):
        t, e, x = map(int, input().split())
        e -= 1
        a, b = edge_list[e]
        if t == 1:
            # a側にxを足す
            if dist[a] < dist[b]:
                # aがroot側の場合は、rootにxを足す
                C[root] += x
                C[b] -= x
            else:
                C[a] += x
        elif t == 2:
            if dist[b] < dist[a]:
                C[root] += x
                C[a] -= x
            else:
                C[b] += x

    # Cについてimos法で更新
    que = deque()
    col = [0]*n
    que.append(root)
    while que:
        pre = que.popleft()
        col[pre] = 1
        for cur in nei_of[pre]:
            if col[cur] == 1:
                continue
            que.appendleft(cur)
            C[cur] += C[pre]

    print(*C, sep='\n')


main()
