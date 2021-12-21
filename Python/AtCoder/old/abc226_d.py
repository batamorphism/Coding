def main():
    n = int(input())
    XY = [tuple(map(int, input().split())) for _ in range(n)]

    magic_list = set()
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            x1, y1 = XY[i]
            x2, y2 = XY[j]
            dx = x2 - x1
            dy = y2 - y1
            if dx > 0:
                sign_x = 1
            elif dx == 0:
                sign_x = 0
            else:
                sign_x = -1
            if dy > 0:
                sign_y = 1
            elif dy == 0:
                sign_y = 0
            else:
                sign_y = -1
            dx = abs(dx)
            dy = abs(dy)
            gcd = gcd_of(dx, dy)
            if gcd == -1:
                dx, dy = 1, 1
            magic_x, magic_y = sign_x * dx // gcd, sign_y * dy // gcd
            magic_list.add((magic_x, magic_y))

    print(len(magic_list))
    # print(magic_list)


def gcd_of(x, y):
    if x == 0 or y == 0:
        return -1
    hi = max(x, y)
    lo = min(x, y)
    q = hi % lo
    while q != 0:
        hi = lo
        lo = q
        q = hi % lo
    return lo


main()
