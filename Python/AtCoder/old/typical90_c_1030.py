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

    # 木の直径を求めればよい
    def get_far_node(st_node):
        dist = [INF]*n
        que = deque()
        que.append(st_node)
        dist[st_node] = 0
        far_node = [st_node, 0]  # 最も遠いnode, 距離
        while que:
            pre = que.popleft()
            d = dist[pre]
            d += 1
            for cur in nei_of[pre]:
                if dist[cur] <= d:
                    continue
                dist[cur] = d
                que.append(cur)
                if d > far_node[1]:
                    far_node[0] = cur
                    far_node[1] = d
        return far_node

    # まずは、0からの距離が最長となるnodeを探す
    st_node = 0
    far_node = get_far_node(st_node)
    st_node = far_node[0]
    far_node = get_far_node(st_node)
    ans = far_node[1]
    print(ans+1)


main()
