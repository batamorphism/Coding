import math

# T[i]の組み合わせのうち、sum(T)/2に最も近づく組み合わせを考える
# すなわち、sum(T)/2を下回るTの組み合わせの最大値を求める
# これは、ナップザック問題である
# dp[i][j] = T[0],...,T[i]からいくつかを選んで和をjにできるか
# dp[i][j] は、d[i-1][j]がTrueの場合True
# そうでない場合は、T[i]を選ぶ必要があり、T[i]を選んだあとjになる必要があることから、d[i-1][j-T[i]]による
# すなわち、dp[i][j] = d[i-1][j] or d[i-1][j-T[i]]
# ただし、i == 0の場合、dp[0][j] = True <=> j = T[0] or j =0
# ただし、j-T[i]<0の場合、d[i-1][j-T[i]] = False


def main():
    N, *T = map(int, open(0).read().split())
    S = sum(T)  # TやSは-1しないので注意
    dp = [[False]*(S+1) for _ in range(N)]

    # 動的計画法
    for i in range(N):
        for j in range(S+1):
            if i == 0:
                if j == T[0] or j == 0:
                    dp[i][j] = True
            elif j-T[i] < 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-T[i]]

    # dp[N-1][j] == Trueを満たすjのうち、s/2を超えるのものを求める
    ans = 1e14
    for i in range(math.ceil(S/2), S+1):
        if dp[N-1][i]:
            ans = i
            break
    print(ans)


main()
