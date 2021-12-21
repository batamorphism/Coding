def main():
    q = int(input())  # データセットの数
    X = []
    Y = []
    for _ in range(q):
        x = input()
        y = input()
        X.append(x)
        Y.append(y)

    # DP = [[0]*(1000+1) for _ in range(1000+1)]

    for i in range(q):
        ans = lcs(X[i], Y[i])
        print(ans)


def lcs(X: str, Y: str) -> int:
    # DP[i][j] を、X[:i], Y[:j]のlcsの長さとする
    # DP[0][*] == 0
    # DP[*][0] == 0
    # X[i-1] == Y[i-1]ならば、DP[i][j] == DP[i-1][j-1]+1
    # それ以外は、DP[i][j] == max(DP[i][j-1], DP[i-1][j])
    len_x = len(X)
    len_y = len(Y)
    DP = [[0]*(len_y+1) for _ in range(len_x+1)]
    for i in range(len_x+1):
        for j in range(len_y+1):
            if i == 0 or j == 0:
                DP[i][j] = 0
                continue
            if X[i-1] == Y[j-1]:
                DP[i][j] = DP[i-1][j-1]+1
            else:
                DP[i][j] = max(DP[i][j-1], DP[i-1][j])
    return DP[len_x][len_y]


main()
