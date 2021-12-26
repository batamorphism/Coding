mod = 998244353


def main():
    r_end, c_end, k = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    # (x1, y1)のパターン数をa
    # (x1, *)のパターン数をb
    # (*, y1)のパターン数をc
    # それ以外をdとする

    a, b, c, d = 1, 0, 0, 0
    for _ in range(k):
        a_nex = b*(c_end-1)+c*(r_end-1)
        b_nex = a+b*(c_end-2)+d*(r_end-1)
        c_nex = a+c*(r_end-2)+d*(c_end-1)
        d_nex = b+c+d*(r_end+c_end-4)  # ここは常に正となる
        a_nex %= mod
        b_nex %= mod
        c_nex %= mod
        d_nex %= mod
        a, b, c, d = a_nex, b_nex, c_nex, d_nex

    # print(a, b, c, d)
    # x2, y2がa, b, c, dのどれに該当するか
    if x1 == x2 and y1 == y2:
        ans = a
    elif x1 == x2:
        ans = b
    elif y1 == y2:
        ans = c
    else:
        ans = d
    print(ans)


main()
