# DP
# 0->i->i+1からなる三角形を、a_iと置く
# 各a_iから辺を1個以上切らなければならない
# 辺0->iを切った時を0、辺0->i+1を切った時を1、辺i->i+1を切った時を2とする
# DP[i][0] = DP[i-1][1]
# DP[i][1] = min(DP[i-1]) + w1_i
# DP[i][2] = min(DP[i-1]) + w2_i
# ただし、i = 1とi=nの時は別途処理する
INF = float('inf')


def main():
    n = int(input())
    n_end = n + 1
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [(-1, -1)]
    # C[i] = (w1_i, w2_i)
    for i in range(1, n_end):
        w1 = A[i % n]
        w2 = B[i-1]
        C.append((w1, w2))

    ans = INF
    for kbn in range(3):
        DP = [[0] * 3 for _ in range(n_end)]
        w1, w2 = C[1]
        if kbn == 0:
            # i == 1の三角形を、0で切った場合
            # i == nの時は、1で切らなければならない
            DP[1][0] = 0
            DP[1][1] = INF
            DP[1][2] = INF
        elif kbn == 1:
            # i == 1の三角形を、1で切った場合
            # 最後の三角形の指定はなし
            DP[1][0] = INF
            DP[1][1] = w1
            DP[1][2] = INF
        else:
            # i == 1の三角形を、2で切った場合
            # 最後の三角形の指定はなし
            DP[1][0] = INF
            DP[1][1] = INF
            DP[1][2] = w2
        for i in range(2, n_end):
            w1, w2 = C[i]
            if i == n and kbn == 0:
                DP[i][0] = INF
                DP[i][1] = min(DP[i-1]) + w1
                DP[i][2] = INF
                break
            DP[i][0] = DP[i-1][1]
            DP[i][1] = min(DP[i-1]) + w1
            DP[i][2] = min(DP[i-1]) + w2
        ans = min(ans, min(DP[n]))
        print(ans)

    # 全て、辺2だった場合は二部グラフにならない
    if ans == sum(A):
        arr = []
        # a_i-b_i a_i-b_i-1ののうち最小のものをansに加算
        for i in range(n):
            a_i = A[i]
            b_i = B[i]
            b_i_1 = B[(i-1) % n]
            arr.append(min(a_i-b_i, a_i-b_i_1))
        ans += sum(arr)
    print(ans)


main()
