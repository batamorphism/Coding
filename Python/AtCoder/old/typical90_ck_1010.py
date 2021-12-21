Bit_max = 10**6
Data = [0]*(Bit_max+10)
INF = 10**9
mod = 10**9+7


def add(pos, val):
    pos += 1
    while pos < Bit_max:
        Data[pos] += val
        pos += pos & -pos


def get_sum(pos):
    # pos以下の値を合計
    pos += 1
    ret = 0
    while pos > 0:
        ret += Data[pos]
        pos -= pos & -pos
    return ret


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    # Aを座標圧縮
    A_dict = {a: i+1 for i, a in enumerate(sorted(list(set(A))))}
    B = [A_dict[a] for a in A]
    B = [0]+B  # 1-ordered
    # [l, r]の転倒数がk以下となる最小のlの値をcl[r]とする
    cl = [i for i in range(n+1)]
    # set cl
    # 尺取り法
    le_i = n
    ri_i = n
    cnt = 0
    add(B[le_i], 1)  # 要素に追加
    while ri_i >= 1:
        while (le_i >= 1 and cnt <= k):
            le_i -= 1
            cnt += get_sum(B[le_i]-1)  # B[le_i]より小さい数の個数を追加
            add(B[le_i], 1)
        add(B[ri_i], -1)
        cnt -= get_sum(Bit_max)-get_sum(B[ri_i])
        cl[ri_i] = le_i+1  # 一個前ならcnt <= kで、現在はcnt > kであるので、一個前を追加
        ri_i -= 1

    # DP
    # DP[r] = Aの要素をr個足した場合の、分割方法の総数
    # DP[0] = 1
    # DP[r] = DP[cl[r]-1]   [cl[r],r]で一つ
    #        +DP[cl[r]]     [cl[r]+1,r]で一つ
    #        +DP[cl[r]+1]   [cl[r]+2,r]で一つ
    #     ...+DP[r-2]       [r-1,r]で一つ
    #        +DP[r-1]       [r,r]で一つ
    # 累積和のために
    # DP2[r] = DP[0]+...+DP[r]を定義する
    # DP[-1] = 0
    # DP[r] = DP2[r-1]-DP2[cl[r]-2]
    DP = [0]*(n+1)
    DP2 = [0]*(n+1)

    DP[0] = 1
    DP2[0] = 1

    for r in range(1, n+1):
        if cl[r]-2 >= 0:
            dp_r = DP2[r-1]-DP2[cl[r]-2]
        else:
            dp_r = DP2[r-1]-DP2[cl[r]-2]
        DP[r] = dp_r % mod
        DP2[r] = (DP2[r-1]+dp_r) % mod

    print(DP[-1])


main()
