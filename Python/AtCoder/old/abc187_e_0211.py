from collections import deque


# 木のimos
# rootを0とする
# fr, to のedge(fr側をroot側、to側をleaf側とする)について
# fr側に+xする場合、rootに+=x, toに-=xする
# to側に+xする場合、toに+=xする
# 行きがけに数字を拾って、加算していけばよい
def main():
    node_end = int(input())
    nei_of = [[] for _ in range(node_end)]
    edge_list = []
    for _ in range(node_end-1):
        fr, to = map(lambda x: int(x)-1, input().split())
        nei_of[fr].append(to)
        nei_of[to].append(fr)
        edge_list.append((fr, to))
    q = int(input())
    query_list = []
    for _ in range(q):
        t, e, x = map(int, input().split())
        e -= 1
        query_list.append((t, e, x))

    # rootからの距離を求める
    INF = float('inf')
    que = deque()
    que.append(0)
    dist = [INF]*node_end
    dist[0] = 0
    while que:
        pre = que.popleft()
        pre_d = dist[pre]
        cur_d = pre_d + 1
        for cur in nei_of[pre]:
            if dist[cur] <= cur_d:
                continue
            dist[cur] = cur_d
            que.append(cur)

    imos = [0]*node_end
    for t, e, x in query_list:
        fr, to = edge_list[e]
        if dist[fr] > dist[to]:
            fr, to = to, fr
            t = 3 - t
        # frがroot側
        if t == 1:
            # root側に追加
            imos[0] += x
            imos[to] -= x
        elif t == 2:
            # leaf側に追加
            imos[to] += x
        else:
            raise

    # DFSで行きがけに累積和を取る
    que = deque()
    que.append(0)
    col = ['w']*node_end
    col[0] = 'b'
    while que:
        pre = que.popleft()
        for cur in nei_of[pre]:
            if col[cur] == 'b':
                continue
            col[cur] = 'b'
            imos[cur] += imos[pre]
            que.append(cur)

    print(*imos, sep='\n')


main()
