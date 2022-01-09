# AからAへの置換Pを考える
# P は [0, ..., n-1]からなる
# Pの先頭i要素まで決定した状態をbitとする
# i = pop_count(bit)である


def main():
    n, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    INF = float('inf')
    ALL = 1 << n
    DP = [INF]*ALL

    # 配るDP
    DP[0] = 0  # DP[null] = 0
    for sub_P in range(ALL):
        # i -> 既に確定したPの要素数
        i = pop_count(sub_P)
        for nex in range(n):
            if (sub_P >> nex) & 1:
                continue
            nex_P = sub_P | (1 << nex)
            # nexをiまでもってくる
            # sub_Pに含まれない要素のうち、nexより小さいものの数
            com_P = (ALL-1) ^ sub_P
            swap_cnt = pop_count(com_P & ((1 << nex)-1))
            # nexとiをswapしたので、xに係るコストはA[nex]とB[i]の差文となる
            cost = DP[sub_P] + abs(A[nex] - B[i])*x + swap_cnt*y
            DP[nex_P] = min(DP[nex_P], cost)

    ans = DP[ALL-1]
    print(ans)


def pop_count(sub_A):
    # 1の個数を数える
    return bin(sub_A).count('1')


main()
