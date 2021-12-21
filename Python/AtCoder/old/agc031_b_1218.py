# 1-indexed
# 出来上がる列と、操作を一対一対応させる
# 同じ数列になるときは、最も細かい操作を左から順に行うものとする
# 1 2 3 1 4 5 1を全て1にする操作は
# 1 1 1 1 4 5 1
# 1 1 1 1 1 1 1
# として作成する（いきなり両端を選ばない）
# DP[i] = 左端からi番目の石まで見たときの、色の塗られ方の場合の数
# i番目の石について何も操作しない場合、DP[i-1]となる
# i番目の石について操作する場合は、前回C[i]が出てきた場所をjとして
# DP[j]となる。
# ただし、j = i-1の場合、DP[i-1]と重複する
from collections import defaultdict
mod = 10**9+7


def main():
    n = int(input())
    stones = [-1] + [int(input()) for _ in range(n)]
    # 貰うDPは1-indexed
    n_end = n+1
    DP = [0] * n_end
    bef_index_of_col_of = defaultdict(int)

    DP[0] = 1
    for i in range(1, n_end):
        col = stones[i]
        bef_index_of_col = bef_index_of_col_of[col]
        if bef_index_of_col == 0:
            # 今まで同じ石が出てきたことがない
            DP[i] = DP[i-1]
        elif bef_index_of_col == i-1:
            # 一個前と同じ石
            DP[i] = DP[i-1]
        else:
            dp = DP[bef_index_of_col]
            DP[i] = DP[i-1] + dp
        DP[i] %= mod
        bef_index_of_col_of[col] = i

    ans = DP[n]
    print(ans)


main()
