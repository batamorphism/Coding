import heapq


# 楽しさ+各地点の標高という量を考える
# x -> y は、楽しさはh_x - h_y 増加し、標高はh_y - h_x 減少するため、+=0
# x <- y は、楽しさは2*(h_y - h_x) 減少し、標高はh_y - h_x 増加するため、 -= (hy - hx)
# 最終的に、楽しさが最大になるようにするため、これが最大となるものを求める
def main():
    node_end, edge_end = map(int, input().split())
    H = list(map(int, input().split()))
    nbh_of = [[] for _ in range(node_end)]

    def calc_cost(fr, to):
        if H[fr] > H[to]:
            return 0
        else:
            return H[to] - H[fr]

    for _ in range(edge_end):
        fr, to = map(lambda x: int(x)-1, input().split())
        cost = calc_cost(fr, to)
        nbh_of[fr].append((to, cost))
        cost = calc_cost(to, fr)
        nbh_of[to].append((fr, cost))

    INF = float('inf')
    dist = [INF] * node_end
    dist[0] = -H[0]
    que = [(-H[0], 0)]
    while que:
        pre_d, pre_node = heapq.heappop(que)
        if pre_d > dist[pre_node]:
            continue
        for cur_node, cur_cost in nbh_of[pre_node]:
            cur_d = pre_d + cur_cost
            if dist[cur_node] <= cur_d:
                continue
            dist[cur_node] = cur_d
            heapq.heappush(que, (cur_d, cur_node))

    ans = 0
    # d = -楽しさ-標高
    for node, d in enumerate(dist):
        happy = -d - H[node]
        ans = max(ans, happy)

    print(ans)


main()
