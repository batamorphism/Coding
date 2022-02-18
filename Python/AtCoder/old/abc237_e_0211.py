# ポテンシャル付きダイクストラ
import heapq


def main():
    node_end, edge_end = map(int, input().split())
    H = list(map(int, input().split()))
    nei_of = [[] for _ in range(node_end)]
    for _ in range(edge_end):
        fr, to = map(lambda x: int(x)-1, input().split())
        nei_of[fr].append(to)
        nei_of[to].append(fr)

    # 楽しさの最大値を求める
    # したがって、楽しさの-1倍を距離として、距離の最小値を求める
    def happy(fr_h, to_h):
        if fr_h > to_h:
            return fr_h-to_h
        else:
            return 2*(fr_h-to_h)

    # ただし、このままだと負辺が出るので、ポテンシャルを付与する
    # ポテンシャル分、距離を加算する
    def pot(node):
        return -H[node]

    def cost(fr, to):
        fr_h, to_h = H[fr], H[to]
        d1 = -happy(fr_h, to_h)
        d2 = pot(to) - pot(fr)
        return d1 + d2

    INF = float('inf')
    dist = [INF]*node_end
    dist[0] = pot(0)
    que = [(pot(0), 0)]
    while que:
        pre_d, pre = heapq.heappop(que)
        if pre_d > dist[pre]:
            continue
        for cur in nei_of[pre]:
            cur_d = pre_d + cost(pre, cur)
            if dist[cur] <= cur_d:
                continue
            dist[cur] = cur_d
            heapq.heappush(que, (cur_d, cur))

    ans = -INF
    for node in range(node_end):
        d = dist[node] - pot(node)
        ans = max(ans, -d)

    print(ans)


main()
