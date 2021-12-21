def main():
    n = int(input())
    # 0~2N-1
    A = list(map(int, input().split()))
    INF = 10**10
    # DP[left][right] = left~right-1を取り除くのにかかるコスト
    # DP[i][i]は1個も取り除かれない
    # DP[i][i+2]はi, i+1を取り除いている
    DP = [[INF]*(2*n+2) for _ in range(2*n+2)]
    for delta in range(2*n+1):
        if delta % 2 == 1:
            continue
        for left in range(2*n+1):
            right = left+delta
            if right >= 2*n+1:
                break
            if delta == 0:
                DP[left][right] = 0
                continue
            mid_cost = DP[left+1][right-1] + abs(A[left]-A[right-1])
            sep_cost = INF
            for sep in range(2*n):
                if left+sep >= 2*n+2:
                    break
                sep_cost = min(DP[left][left+sep]+DP[left+sep][right], sep_cost)
            DP[left][right] = min(sep_cost, mid_cost)

    print(DP[0][2*n])


main()
