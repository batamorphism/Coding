# https://www.youtube.com/watch?v=ReGvflPU81c
# 遅延セグを描きたいときはこれ見ろ
# https://smijake3.hatenablog.com/entry/2018/11/03/100133
INF = 10**12
seg_max = 1 << 15
seg_data = [-INF]*(seg_max*2)


def update(pos, x):
    pos += seg_max
    seg_data[pos] = x
    pos //= 2
    while pos > 0:  # 一番下から上に登りながら更新
        seg_data[pos] = max(seg_data[pos*2], seg_data[pos*2+1])
        pos //= 2


def query(le, ri):
    # [le, ri)の最大値を求める
    ret = -INF
    le += seg_max
    ri += seg_max
    while le < ri:
        if le % 2 != 0:
            ret = max(seg_data[le], ret)
            le += 1
        le //= 2
        if ri % 2 != 0:
            ret = max(seg_data[ri-1], ret)
            ri -= 1
        ri //= 2
    return ret


def main():
    weight, n = map(int, input().split())
    stuff_list = []
    for _ in range(n):
        stuff = tuple(map(int, input().split()))
        stuff_list.append(stuff)
    # DP[i][w] = 料理i番目まで見たときの、香辛料をw使った際の価値の最大値
    # DP[i][w] = max(DP[i-1][w], DP[i-1][w-ri]+v, ..., DP[i-1][w-le]+v)
    update(0, 0)
    for le, ri, v in stuff_list:
        for w in range(weight, -1, -1):
            dp1 = query(w, w+1)
            dp2 = query(max(w-ri, 0), max(w-le+1, 0))+v
            update(w, max(dp1, dp2))

    ans = query(weight, weight+1)
    if ans < 0:
        ans = -1
    print(ans)


main()
