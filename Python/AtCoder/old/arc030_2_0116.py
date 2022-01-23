from collections import deque


# DFSの到達経路順を求めて
# 各経路の距離を求める。これはlcaとか使わんでも間に合う
def main():
    INF = float('inf')
    node_end, x = map(int, input().split())
    x -= 1
    H = list(map(int, input().split()))
    H[x] = 1

    nei_of = [[] for _ in range(node_end)]
    for _ in range(node_end-1):
        a, b = map(lambda x: int(x)-1, input().split())
        nei_of[a].append(b)
        nei_of[b].append(a)

    route = [-1]*node_end

    color = ['w']*node_end
    color[x] = 'b'
    que = deque()
    que.append(x)
    cnt = 0
    while que:
        pre = que.popleft()
        route[pre] = cnt
        cnt += 1
        for cur in nei_of[pre]:
            if color[cur] != 'w':
                continue
            que.appendleft(cur)
            color[cur] = 'b'

    def bfs(fr, to):
        # fr->toの距離を求める
        dist = [INF]*node_end
        que = deque()
        que.append(fr)
        dist[fr] = 0
        while que:
            pre = que.popleft()
            pre_d = dist[pre]
            cur_d = pre_d + 1
            for cur in nei_of[pre]:
                if dist[cur] <= cur_d:
                    continue
                dist[cur] = cur_d
                que.append(cur)
        return dist[to]

    path = []
    for i in range(node_end):
        h_i = H[i]
        route_i = route[i]
        if h_i:
            path.append((i, route_i))

    path.sort(key=lambda x: x[1])
    path.append((x, -1))
    # pathの第一要素順に距離を求める
    ans = 0
    for i in range(len(path)-1):
        j = i+1
        fr = path[i][0]
        to = path[j][0]
        ans += bfs(fr, to)

    print(ans)


main()
