def main():
    n = int(input())
    for _ in range(n):
        x = input()
        y = input()
        print(lcs(x, y))


def lcs(x: str, y: str):
    # DP[i][j] = x[:i]とy[:j]のlcs
    # DP[i][j] = もしx[i-1] == y[i-1]ならば、更新可能性あり
    # それ以外は、更新可能性なし
    max_i = len(x)
    max_j = len(y)
    DP = [[0]*(max_j+1) for _ in range(max_i+1)]
    for i in range(max_i+1):
        for j in range(max_j+1):
            if i == 0 or j == 0:
                DP[i][j] = 0
                continue
            if x[i-1] == y[j-1]:
                DP[i][j] = max(DP[i-1][j-1]+1, DP[i][j-1], DP[i-1][j])
            else:
                DP[i][j] = max(DP[i-1][j-1], DP[i][j-1], DP[i-1][j])
    return DP[-1][-1]


main()
