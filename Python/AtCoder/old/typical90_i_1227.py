# 各点p0 2000に対して
# 各点p1 2000個との俯角を計算し
# 最大のものを高速で求める
import math
from collections import deque


def main():
    n = int(input())
    XY = [tuple(map(int, input().split())) for _ in range(n)]

    INF = float('inf')
    ans = -INF
    for i0, p0 in enumerate(XY):
        degree_list = []
        for i1, p1 in enumerate(XY):
            if i0 == i1:
                continue
            # p0 -> (1, 0)とp0 -> p1のなす角を求める
            inner_product = (p1[0] - p0[0])*1 + (p1[1] - p0[1])*0
            cos_theta = inner_product / math.sqrt((p1[0] - p0[0])**2 + (p1[1] - p0[1])**2)
            theta = math.acos(cos_theta)
            degree = math.degrees(theta)
            if (p1[1]-p0[1]) < 0:
                degree = 360 - degree
            degree_list.append(degree)
        # 円環は2倍
        degree_list += [degree+360 for degree in degree_list]
        degree_list.sort()
        max_degree = -INF
        que = deque()  # queの先頭と末尾のなす角度を最大化する
        last_degree = degree_list[0]
        for degree in degree_list:
            que.append(degree)
            front_degree = degree
            cur_degree = (front_degree - last_degree) % 360
            max_degree = max(max_degree, min(cur_degree, 360-cur_degree))
            while que and not cur_degree <= 180:
                rm = que.popleft()
                last_degree = rm
                cur_degree = (front_degree - last_degree) % 360
                max_degree = max(max_degree, min(cur_degree, 260-cur_degree))
        ans = max(ans, max_degree)

    print(ans)


main()

