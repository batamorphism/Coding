import sys

# 再帰できる上限を引き上げる
sys.setrecursionlimit(200000)

memo = {}


def main():

    # 動的計画法
    # 文字列textに対して、題意を満たす組み合わせをd(8, text)とする
    # また、chokudaに対して題意を満たす組み合わせをd(7, text)とする
    # 以下、文字数に対応してd(1, text)まで定義する
    # 
    # sの部分列s[:k](先頭k文字まで)について、
    # k+1文字目s[k]がchokudai以外であれば、
    #   d(8, s[:k+1]) = d(8, s[:k])
    # i以外であった場合も同様
    # iであった場合、d(8, s[:k+1]) = d(8, s[:k]) + d(7, s[:k])
    # 以下同様

    # textの先頭n桁について、題意を満たす組み合わせをd[8][n]とする
    # また、chokudaに対して題意を満たす組み合わせをd[7][n]とする
    # ただし、d[0][*]の時は1
    # ただし、d[*][0]の時は0
    # この時、d[7][i]=d[7][i-1] + d[6][i-1]

    s, *_ = open(0).read().split()
    t = 'chokudai'
    n = len(s)
    d = [[0 for _ in range(9)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(9):
            if j == 0:
                d[i][j] = 1
            elif j == 0:
                d[i][j] = 0
            else:
                if s[i-1] == t[j-1]:
                    d[i][j] = d[i-1][j-1] + d[i-1][j]
                else:
                    d[i][j] = d[i][j-1]

    print(d[8][n-1])


main()
