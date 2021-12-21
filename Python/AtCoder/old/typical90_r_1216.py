import math


def main():
    T = int(input())
    L, x, y = map(int, input().split())

    q = int(input())
    query_list = [int(input()) for _ in range(q)]

    for query in query_list:
        ans = solve(L, T, x, y, query)
        print(ans)


def solve(L, T, x, y, e):
    # 今の観測者の座標を求める
    v1 = (0, 0, L/2)
    rad = 2*math.pi/T*e
    v2 = (0, -math.sin(rad)*L/2, -math.cos(rad)*L/2)
    my_pos = (v1[0]+v2[0], v1[1]+v2[1], v1[2]+v2[2])

    your_pos = (x, y, 0)
    vect = (your_pos[0]-my_pos[0], your_pos[1]-my_pos[1], your_pos[2]-my_pos[2])
    h = vect[2]
    w = (vect[0]**2+vect[1]**2)**0.5
    tan_me_you = -h/w
    rad_me_you = math.atan(tan_me_you)
    deg_me_you = math.degrees(rad_me_you)
    return deg_me_you


main()
