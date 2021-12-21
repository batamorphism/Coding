# DP[n][w] := n番目までのアイテムを使って重さがちょうどwとなるような料理を選んだときの価値の最大値
# DP[n][w] = max(DP[n-1][w], DP[n-1][w-w_hi] + v_n, ..., DP[n-1][w-w_lo] + v_n)
# ここで、w_hi, w_loはn番目のアイテムの重さの上限と下限を表す
# max(DP[n-1][w-w_hi], ...,DP[n-1][w-w_lo])を求めるために、segment treeを使う
INF = 10**18

# seg_tree
seg_max = 10**5
seg_tree = [-INF]*(2*seg_max)


def update(pos, val):
    pos += seg_max
    seg_tree[pos] = val
    pos >>= 1
    while pos > 0:
        seg_tree[pos] = max(seg_tree[pos*2], seg_tree[pos*2+1])
        pos >>= 1


def query(le, ri):
    res = -INF
    le += seg_max
    ri += seg_max
    while le < ri:
        if le % 2 == 1:
            res = max(res, seg_tree[le])
            le += 1
        if ri % 2 == 1:
            ri -= 1
            res = max(res, seg_tree[ri])
        le >>= 1
        ri >>= 1
    return res


def main():
    W, N = map(int, input().split())
    item_list = [tuple(map(int, input().split())) for _ in range(N)]
    update(0, 0)

    for item in item_list:
        w_lo, w_hi, v = item
        for w in range(W, -1, -1):
            # DP[n][w] = max(DP[n-1][w], DP[n-1][w-w_hi] + v_n, ..., DP[n-1][w-w_lo] + v_n)
            dp1 = query(w, w+1)
            dp2 = query(max(w-w_hi, 0), max(w-w_lo+1, 0)) + v
            # print(item, w, dp1, dp2)
            update(w, max(dp1, dp2))

    ans = query(W, W+1)
    if ans < 0:
        ans = -1
    print(ans)


main()
