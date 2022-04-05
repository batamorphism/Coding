from collections import defaultdict
MOD = 998244353


def main():
    n = int(input())
    A = list(map(int, input().split()))
    bef_of = defaultdict(lambda: -1)
    # 配るDP
    DP = [0]*(n+10)
    DP[0] = 1
    sum_a = 0
    for i, a_i in enumerate(A):
        sum_a += a_i
        bef_i = bef_of[sum_a]
        if bef_i == -1:
            DP[i+1] = DP[i]*2
        else:
            DP[i+1] = DP[i]*2 - DP[bef_i]
        bef_of[sum_a] = i
    ans = DP[n-1]
    print(ans)


main()
