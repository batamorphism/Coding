def main():
    ans_list = []
    while True:
        n = int(input())
        W = list(map(int, input().split()))
        if n == 0:
            break
        DP = [[0]*(n+1) for _ in range(n+1)]

        # dは取り除きたい個数
        for d in range(1, n+1):
            for le in range(n+1):
                ri = le+d
                if ri >= n+1:
                    break
                if d % 2 == 1:
                    DP[le][ri] = max(DP[le][ri-1], DP[le+1][ri])
                    continue
                dp = 0
                for sep in range(le, ri, 2):
                    dp = max(dp, DP[le][sep] + DP[sep][ri])
                if DP[le+1][ri-1] == d-2 and le+1 < n+1 and ri-1 >= 0:
                    if abs(W[ri-1]-W[le]) <= 1:
                    # この条件で抜くためには、le～ri-1までのブロックがすでに全部抜いている必要がある
                        dp = max(dp, DP[le+1][ri-1]+2)
                DP[le][ri] = dp
        ans_list.append(DP[0][n])

    for ans in ans_list:
        print(ans)


main()
