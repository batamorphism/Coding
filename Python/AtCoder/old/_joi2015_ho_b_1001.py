def main():
    n = int(input())
    cake_list = [int(input()) for _ in range(n)]
    # DP[i][j] = cake_list[i]~[j]が残っている状態
    # ただし、DP[i][i]はcake_list[i]のみが残っている状態
    # DP[i][i-1]は全てのケーキが残っている状態
    # DP[i][i-] = DP[i][i+n-1]である(mod n)
    DP = [[0]*n for _ in range(n)]

    for delta in range(n):
        for left in range(n):
            right = (left+delta) % n
            ate = (n-delta+1)
            is_me = ((ate % 2) == 0)
            if delta == 0:
                if is_me:
                    DP[left][right] = cake_list[left]
                continue
            if is_me:
                # 左のケーキを先に食べた場合
                score1 = cake_list[left] + DP[(left+1) % n][right]
                # 右のケーキを先に食べた場合
                score2 = cake_list[right] + DP[left][(right-1) % n]
                DP[left][right] = max(score1, score2)
            else:
                if cake_list[right] > cake_list[left]:
                    score = DP[left][(right-1) % n]
                else:
                    score = DP[(left+1) % n][right]
                DP[left][right] = score

    ans = 0
    for left in range(n):
        ans = max(DP[left][(left-1) % n], ans)
    print(ans)


main()
