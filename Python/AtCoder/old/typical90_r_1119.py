import math


def main():
    t = int(input())
    L, x, y = map(int, input().split())
    statue = (x, y, 0)
    ans_list = []

    def calc_pos(time):
        # 時刻tで2pi動く半径L/2の円
        rad = math.pi * 2
        x = math.cos(rad * time / t) * L/2
        y = math.sin(rad * time / t) * L/2
        return (0, -y, L/2 - x)

    q = int(input())
    for _ in range(q):
        e = int(input())
        # 時刻eでの貴女の位置を求める
        pos = calc_pos(e)
        dx = pos[0] - statue[0]
        dy = pos[1] - statue[1]
        dz = pos[2] - statue[2]
        dxy = math.sqrt(dx**2 + dy**2)
        tan_ = dz/dxy
        ans = math.atan(tan_)
        ans = math.degrees(ans)
        ans_list.append(ans)

    print(*ans_list, sep='\n')


main()
