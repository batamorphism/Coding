# 最短経路問題
# 楽しさをマイナスの距離だと思い、node 0 からの距離が最小となるnodeを求める
# ベルマンフォード
import heapq


def main():
    node_end, edge_end = map(int, input().split())
    height_of = list(map(int, input().split()))
    nbh_of = [[] for _ in range(node_end)]

    def calc_happy(fr_h, to_h):
        if fr_h > to_h:
            return fr_h - to_h
        else:
            return 2*(fr_h - to_h)

    for _ in range(edge_end):
        fr, to = map(lambda x: int(x)-1, input().split())
        fr_h = height_of[fr]
        to_h = height_of[to]
        fr2to_dist = -calc_happy(fr_h, to_h)
        to2fr_dist = -calc_happy(to_h, fr_h)
        nbh_of[fr].append((to, fr2to_dist))
        nbh_of[to].append((fr, to2fr_dist))

    INF = float('inf')
    dist = [INF]*node_end
    dist[0] = 0

    que = [(0, 0)]
    while que:
        pre_d, pre = heapq.heappop(que)
        if pre_d > dist[pre]:
            continue
        for cur, cost in nbh_of[pre]:
            cur_d = pre_d + cost
            if cur_d < dist[cur]:
                dist[cur] = cur_d
                heapq.heappush(que, (cur_d, cur))

    print(-min(dist))


main()
