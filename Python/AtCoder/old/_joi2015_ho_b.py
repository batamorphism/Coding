def main():
    n = int(input())
    piece_list = [0]*n
    for i in range(n):
        piece_list[i] = int(input())

    DP = [[0]*n for _ in range(n)]
    for d_i in range(n):
        for i in range(n):
            # i～jのケーキが残っている
            # j-i=d_i すなわち、残ってるケーキ数はd_i+1
            # 既に取ったケーキ数はn-d_i-1 これが偶数だと次はmeがとる
            j = (i + d_i) % n
            is_me_turn = ((n-d_i-1) % 2 == 0)
            if is_me_turn:  # 次はmeがDPを最大化するようpieceをとる
                DP[i][j] = max(piece_list[i]+DP[(i+1) % n][j],
                               piece_list[j]+DP[i][(j-1) % n])
            else:
                if piece_list[i] < piece_list[j]:
                    DP[i][j] = DP[i][(j-1) % n]
                else:
                    DP[i][j] = DP[(i+1) % n][j]

    ans = 0
    for i in range(n):
        j = (i-1) % n
        ans = max(ans, DP[i][j])

    print(ans)


main()
