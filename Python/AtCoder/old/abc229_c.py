# DPはWが大きいのでTLE
# a_iが大きい順に、最大までチーズを乗っけていく
def main():
    n, w = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(n)]
    AB.sort(reverse=True)
    ans = 0
    for a, b in AB:
        # print(a, b)
        if w >= b:
            # 全部使う
            w -= b
            ans += a*b
        else:
            # wだけつかう
            ans += w*a
            w = 0
            break
    print(ans)


main()
