# しゃくとり法
import math
from collections import deque


def points2degree(p0, p1):
    # 角x軸,p0,p1のなす角を返す
    vec1 = p1[0] - p0[0], p1[1] - p0[1]

    # 単位ベクトルにする
    len_vec1 = math.sqrt(vec1[0] ** 2 + vec1[1] ** 2)
    vec1 = vec1[0] / len_vec1, vec1[1] / len_vec1

    # x軸とのなす角を求める
    cos_theta = min(vec1[0], 1)
    theta = math.acos(cos_theta)  # 0~pi
    degree = theta * 180 / math.pi
    if vec1[1] < 0:
        degree = 360 - degree
    return degree


def fix_degree(degree):
    # 0~360の角度を、0~180に変換
    degree = degree % 360
    if degree > 180:
        degree = 360 - degree
    return degree


def main():
    n = int(input())
    p_list = []
    for _ in range(n):
        x, y = map(int, input().split())
        p_list.append((x, y))

    ans = -1
    for i, p0 in enumerate(p_list):
        # x軸とのなす角を求める
        degree_list = []
        for p1 in p_list:
            if p0 != p1:
                degree = points2degree(p0, p1)
                degree_list.append(degree)
        # dgree_listの中から2つ選んで、差が180度に最も近いものを求める
        # 円環は2倍
        cycle_degree_list = degree_list[:]
        for degree in degree_list:
            cycle_degree_list.append(degree + 360)
        cycle_degree_list.sort()
        # 角度の差を足し合わせて、最も180度に近いものを求めればよい
        delta_degree_list = []
        for i in range(len(cycle_degree_list) - 1):
            delta_degree_list.append(cycle_degree_list[i + 1] - cycle_degree_list[i])

        # しゃくとり法
        que = deque()
        cur_degree = 0
        for degree in delta_degree_list:
            cur_degree += degree
            que.append(degree)
            ans = max(ans, fix_degree(cur_degree))
            while que and not cur_degree <= 180:
                rm = que.popleft()
                cur_degree -= rm
                ans = max(ans, fix_degree(cur_degree))

    print(ans)


main()
