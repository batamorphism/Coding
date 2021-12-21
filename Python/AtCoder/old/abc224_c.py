def main():
    n = int(input())
    p_list = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for p1_i in range(n):
        for p2_i in range(p1_i, n):
            for p3_i in range(p2_i, n):
                p1, p2, p3 = p_list[p1_i], p_list[p2_i], p_list[p3_i]
                x1, y1 = p1
                x2, y2 = p2
                x3, y3 = p3
                a1x = x1 - x2
                a1y = y1 - y2
                a2x = x1 - x3
                a2y = y1 - y3
                s = abs(a1x*a2y-a1y*a2x)
                if s > 0:
                    ans += 1
    print(ans)


main()
