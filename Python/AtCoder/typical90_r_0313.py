import math


def main():
    t = int(input())
    l, x, y = map(int, input().split())
    q = int(input())
    for _ in range(q):
        e = int(input())
        solve(t, l, x, y, e)


def solve(t, l, x, y, e):
    vec_to = [x, y, 0]  # 像の場所
    vec1 = [0, 0, 0]  # 観覧車の足元まで
    vec2 = [0, 0, l/2]  # 観覧車の中央まで
    theta = e/t*2*math.pi
    # (0, -sin, -cos)
    vec3 = [0, -math.sin(theta)*l/2, -math.cos(theta)*l/2]
    vec_fr = [vec1[i] + vec2[i] + vec3[i] for i in range(3)]

    vec = [vec_to[i] - vec_fr[i] for i in range(3)]
    x, y, z = vec
    w = (x**2 + y**2)**0.5
    h = z
    theta2 = math.degrees(math.atan(h/w))
    theta2 *= -1
    print(theta2)


main()
