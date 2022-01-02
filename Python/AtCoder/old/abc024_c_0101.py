# 貪欲に移動
def main():
    n, d_end, k = map(int, input().split())
    LR = [tuple(map(int, input().split())) for _ in range(d_end)]
    INF = float('inf')

    # le, ri = LR[d]
    # d日目に、[le, ri]にいる民族は移動する
    item_list = [tuple(map(int, input().split())) for _ in range(k)]
    for item in item_list:
        st, en = item
        cur = st
        ans = INF
        for d, lr in enumerate(LR):
            le, ri = lr
            if le <= cur <= ri:
                # 移動可能
                # enに近いほうに移動する
                if le <= en <= ri:
                    # 到着
                    cur = en
                    ans = d+1
                    break
                elif en < cur:
                    # 左に移動
                    cur = le
                elif cur < en:
                    # 右に移動
                    cur = ri
                elif cur == en:
                    # 何もしない
                    pass
                else:
                    raise
        if ans == INF:
            raise
        print(ans)


main()
