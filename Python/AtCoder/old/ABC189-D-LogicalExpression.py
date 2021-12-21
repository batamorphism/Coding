# N = 60
# 2**60 = 1e18 bit全探索は無理
# y[n] == Trueの時
# y[n-1]は、S[n]がANDだったならば、True
# S[n]がORだったならば、x[n]がTrueだったならばFalseもしくはTrue、そうでないならば、True
# DP[i][bool] = y[i] == boolとなるxの組み合わせ
# boolがTrueの場合、S[

def main():
    n = int(input())
    S = ['None']
    for _ in range(n):
        S.append(input())

    DP = [[-1]*2 for _ in range(n+1)]
    DP[0][0] = 1    # x[0] = Falseのみ
    DP[0][1] = 1    # x[0] = Trueのみ

    for i in range(1, n+1):
        for bit in range(2):
            if bit == 1:
                # y[i] = Trueの時
                if S[i] == 'AND':
                    DP[i][bit] = DP[i-1][1]  # y[i-1]がTrueのとき, x[i]=Trueの1通り
                else:
                    DP[i][bit] = DP[i-1][1]*2+DP[i-1][0]
            else:
                if S[i] == 'AND':
                    DP[i][bit] = DP[i-1][1]+DP[i-1][0]*2
                else:
                    DP[i][bit] = DP[i-1][0]

    print(DP[n][1])


main()