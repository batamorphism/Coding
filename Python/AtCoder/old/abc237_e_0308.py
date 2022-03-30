import heapq


def main():
    node_end, edge_end = map(int, input().split())
    H = list(map(int, input().split()))
    nei_of = [[] for _ in range(node_end)]

    for _ in range(edge_end):
        fr, to = map(lambda x: int(x) - 1, input().split())
        nei_of[fr].append(to)
        nei_of[to].append(fr)

    # ポテンシャル付きダイクストラ
    # ポテンシャルを、Hそのものとする
    def happy_of(fr, to):
        pot = H[to] - H[fr]
        if H[fr] > H[to]:
            happy = H[fr] - H[to]  # potを足すと、常に0
        else:
            happy = (H[fr] - H[to])*2  # potを足すと、常に負
        return pot+happy

    def cost_of(fr, to):
        ret = -happy_of(fr, to)
        if ret < 0:
            raise
        return -happy_of(fr, to)

    # -happy_ofをコストとしたダイクストラにより
    # 楽しさの減少が最小のものを計算できる
    INF = float('inf')
    dist = [INF]*node_end
    dist[0] = 0
    que = [(0, 0)]  # (dist, node)
    while que:
        pre_dist, pre_node = heapq.heappop(que)
        if dist[pre_node] < pre_dist:
            continue
        for cur_node in nei_of[pre_node]:
            cur_cost = cost_of(pre_node, cur_node)
            cur_dist = pre_dist + cur_cost
            if dist[cur_node] <= cur_dist:
                continue
            dist[cur_node] = cur_dist
            heapq.heappush(que, (cur_dist, cur_node))

    ans = -INF
    for node in range(node_end):
        d = dist[node]
        pot = H[node] - H[0]
        happy = -d-pot
        ans = max(ans, happy)
    print(ans)


main()
