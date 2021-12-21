# ナップザック問題

def main():
    n = int(input())
    x, y = map(int, input().split())
    A = [0]
    B = [0]
    for _ in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    DP = [[[1000]*301 for _ in range(301)] for _ in range(301)]

    # DP[i][x][y] = i番目まで見て、たこ焼きx個たい焼きy個が実現可能な弁当数
    # init
    for i in range(n):
        DP[i][0][0] = 0

    for i in range(1, n+1):
        for curr_x in range(x+1):
            for curr_y in range(y+1):
                DP[i][curr_x][curr_y] = min(DP[i-1][max(curr_x-A[i], 0)][max(curr_y-B[i], 0)]+1,
                                            DP[i-1][curr_x][curr_y]
                                            )

    if DP[n][x][y] == 1000:
        print(-1)
    else:
        print(DP[n][x][y])


main()
