# 2点間距離
# 全点間距離は間に合う(O(10**6))
# 通る順序は、DFSで通った順序
def main():
    node_end, root = map(int, input().split())
    root -= 1
    H = list(map(lambda x: int(x), input().split()))
    H[root] = 1
    nei_of = [set() for _ in range(node_end)]
    for _ in range(node_end-1):
        fr, to = map(lambda x: int(x)-1, input().split())
        nei_of[fr].add(to)
        nei_of[to].add(fr)

    # dfsでとおった順序を計算
    order = [-1]*node_end
    cur_order = 0
    que = [root]
    while que:
        pre = que.pop()
        order[pre] = cur_order
        cur_order += 1
        for cur in nei_of[pre]:
            if order[cur] != -1:
                continue
            que.append(cur)

    # 全点間距離を計算
    INF = float('inf')
    dist = [[INF]*node_end for _ in range(node_end)]
    for k in range(node_end):
        for fr in range(node_end):
            for to in range(node_end):
                # 1. 直通
                if fr in nei_of[to]:
                    dp1 = 1
                else:
                    dp1 = INF
                # 2. kを経由
                dp2 = dist[fr][k] + dist[k][to]
                # 3. kを経由しない
                dp3 = dist[fr][to]
                # 4. そもそも同じ
                if fr == to:
                    dp4 = 0
                else:
                    dp4 = INF
                dist[fr][to] = min(dp1, dp2, dp3, dp4)

    # Hが1のノードを、order順に追加
    path = [node for node in range(node_end) if H[node] == 1]
    path.sort(key=lambda x: order[x])
    if path[0] != root:
        raise
    path.append(root)

    # path順に巡っていく
    ans = 0
    for i in range(len(path)-1):
        fr = path[i]
        to = path[i+1]
        ans += dist[fr][to]
    print(ans)


main()
