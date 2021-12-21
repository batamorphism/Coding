from collections import deque
import math

# 各node毎に、他のノードまでの角度を格納する
# 角度が360度回転するまで、しゃくとり法
# しゃくとり法は、なす角が180度を超えるまで先に進め、180度を下回るまで後ろを取り除く


def main():
    n = int(input())
    point_list = [tuple(map(int, input().split())) for _ in range(n)]

    edges_of = [[] for _ in range(n)]
    for fr in range(n):
        for to in range(n):
            if fr == to:
                continue
            # x軸と、frからtoへの角度を求める
            dx = point_list[to][0] - point_list[fr][0]
            dy = point_list[to][1] - point_list[fr][1]
            deg = math.degrees(math.atan2(dy, dx))
            edges_of[fr].append(deg)

    for edges in edges_of:
        edges.sort()

    # 各edgeについて、x軸との角度ではなく、前のedgeとの差分にする
    for edges in edges_of:
        for i in range(len(edges)-1, 0, -1):
            edges[i] -= edges[i-1]
        edges[0] = 0

    # しゃくとり法
    ans = 1000
    for node in range(n):
        que = deque()
        deg = 0
        for edge in edges_of[node][1:]:
            # print(que, ans)
            que.appendleft(edge)
            deg += edge
            deg %= 360
            ans = min(ans, abs(180-deg))
            while que and not deg < 180:
                rm = que.pop()
                deg -= rm
                deg %= 360
                ans = min(ans, abs(180-deg))

    print(180-ans)


main()
