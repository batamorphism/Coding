# 同じ色のボールがたくさんあっても、重要なのは左端と右端にあるボールのみ
# したがって、各色のボールは高々2個としてよい
# DP
# DP[i][lr] = i番目のボールとして、最後にleかriを取った場合の、コストの最小値
# DP[i][le] = min(DP[i-1][le] + cost(i-1, le, le), DP[i-1][ri] + cost(i-1, ri, le))
def main():
    n = int(input())
    # lr_of[col] = [le, ri]
    # 1-indexed
    LE = 0
    RI = 1
    INF = float('inf')
    lr_of = [[INF, -INF] for _ in range(n+2)]
    exists = [0]*(n+2)
    for _ in range(n):
        x, c = map(int, input().split())
        lr_of[c][LE] = min(lr_of[c][LE], x)
        lr_of[c][RI] = max(lr_of[c][RI], x)
        exists[c] = 1

    lr_of[0][LE] = 0
    lr_of[0][RI] = 0
    lr_of[n+1][LE] = 0
    lr_of[n+1][RI] = 0
    exists[0] = 1
    exists[n+1] = 1

    DP = [[INF] * 2 for _ in range(n+2)]
    DP[0][LE] = 0
    DP[0][RI] = 0

    def cost(pre_col, cur_col, pre_lr, nex_lr):
        # pre_col: 前のボールの色
        # pre_lr: 前のボールのlr
        pre_x = lr_of[pre_col][pre_lr]
        nex_x = lr_of[cur_col][nex_lr]
        way_x = lr_of[cur_col][1 ^ nex_lr]
        # pre_x -> way_x -> nex_xの順に経由する
        cost = abs(pre_x - way_x) + abs(way_x - nex_x)
        return cost

    pre_i = 0
    for i in range(1, n+2):
        if not exists[i]:
            continue
        for lr in range(2):
            dp = INF
            dp = min(dp, DP[pre_i][LE] + cost(pre_i, i, LE, lr))
            dp = min(dp, DP[pre_i][RI] + cost(pre_i, i, RI, lr))
            DP[i][lr] = dp
        pre_i = i

    ans = min(DP[n+1])
    # print(DP)
    print(ans)


main()
