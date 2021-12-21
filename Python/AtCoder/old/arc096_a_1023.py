INF = 10**9


def main():
    a, b, c, x, y = map(int, input().split())
    # cを買う数で全探索する
    c_end = max(x*2, y*2)+1
    ans = INF
    for c_cnt in range(c_end):
        a_cnt = max(x-c_cnt//2, 0)
        b_cnt = max(y-c_cnt//2, 0)
        cost = a_cnt*a+b_cnt*b+c_cnt*c
        ans = min(cost, ans)

    print(ans)


main()
