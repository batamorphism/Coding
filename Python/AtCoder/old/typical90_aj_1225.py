# import numpy as np

"""
# (1, 1) -> (1, 0)
# (-1, 1) -> (0, 1)
# となる行列Aを作る
inv_A = np.array([[1, 1], [-1, 1]])
A = np.linalg.inv(inv_A)
print(A)
# [[ 0.5 -0.5]
# [ 0.5  0.5]]
# したがって、
# 1 -1
# 1 1
# を作用すると、(2, 0), (0, 2)に45度回転する
# マンハッタン距離は、x座標の差とy座標の差のいずれか大きいほうとなる
"""


def main():
    n, q = map(int, input().split())
    point_list = []
    for _ in range(n):
        x, y = map(int, input().split())
        point_list.append((x, y))

    # rotate
    point_list = [(x-y, x+y) for x, y in point_list]

    x_max = max(point_list, key=lambda x: x[0])
    x_min = min(point_list, key=lambda x: x[0])
    y_max = max(point_list, key=lambda x: x[1])
    y_min = min(point_list, key=lambda x: x[1])

    ans_list = []
    for _ in range(q):
        i = int(input())
        i -= 1
        point = point_list[i]
        ans = -1
        for p in [x_max, x_min, y_max, y_min]:
            ans = max(ans, calc_dist(point, p))
        ans_list.append(ans)

    print(*ans_list, sep='\n')


def calc_dist(p1, p2):
    return max(abs(p1[0]-p2[0]), abs(p1[1]-p2[1]))


main()
