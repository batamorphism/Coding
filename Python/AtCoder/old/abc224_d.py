from collections import deque
INF = 10**9

def main():
    m = int(input())
    edge = []
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edge.append((u, v))
    tmp = list(map(int, input().split()))
    fr_node = [-1]*9
    for i, num in enumerate(tmp):
        fr_node[num-1] = i
    to_node = [0, 1, 2, 3, 4, 5, 6, 7, -1]

    def nei_node(pre_node):
        cur_node = pre_node[:]
        for u, v in edge:
            if pre_node[u] == -1 or pre_node[v] == -1:
                cur_node[u] = pre_node[v]
                cur_node[v] = pre_node[u]
                yield cur_node
                cur_node[u] = pre_node[u]
                cur_node[v] = pre_node[v]

    # bfs
    dist = {}
    que = deque()
    que.append(fr_node)
    dist[tuple(fr_node)] = 0
    while que:
        pre_node = que.popleft()
        d = dist[tuple(pre_node)]
        d += 1
        for cur_node in nei_node(pre_node):
            if dist.get(tuple(cur_node), INF) <= d:
                continue
            dist[tuple(cur_node)] = d
            que.append(cur_node[:])

    print(dist.get(tuple(to_node), -1))


main()
