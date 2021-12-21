# AをBと同じ値の集合にする方法は、18!通りあり、全探索は間に合わない?
# 左端から詰めていく？
# 2**18 = 262144

def main():
    n, x, y = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    B = [0] + list(map(int, input().split()))

    # DP[i][bit] = i番目までそろえた状態で、bitを既に使用した状態でのコストの最小値
    # DP[i][bit] = DP[i-1][pre_bit] + cost(i, j)
    # ここで、cost(i, j)は、a_jをiに持ってきた後、b_iに変更するのにかかるコスト
    ALL = 1 << n
    INF = float('inf')
    DP = [[INF] * ALL for _ in range(n+1)]
    DP[0][0] = 0
    for i in range(1, n+1):
        for bit in range(ALL):
            if bin(bit).count('1') < i:
                continue
            dp = INF
            for j in range(n):
                if bit >> j & 1 == 0:
                    continue
                pre_bit = bit ^ (1 << j)
                # i < j
                bin_bit = bin(pre_bit)[2:].zfill(n)
                cnt_0_i_to_j = 0
                for k in range(i-1, j):
                    if bin_bit[k] == '0':
                        cnt_0_i_to_j += 1
                dp = min(dp, DP[i-1][pre_bit] + abs(A[i] - B[j+1])*x + cnt_0_i_to_j*y)
            DP[i][bit] = dp

    print(DP[n][ALL-1])


main()
