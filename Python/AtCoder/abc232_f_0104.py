def main():
    n, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ALL = 1 << n
    INF = float('inf')
    DP = [INF]*ALL

    # 貰うDP
    for S in range(ALL):
        if S == 0:
            DP[S] = 0
            continue
        num = popcount(S) - 1
        for i, a_i in enumerate(A):
            # Sがiを含むときだけ処理
            if not ((S >> i) & 1):
                continue
            pre_S = S ^ (1 << i)
            # iをnumに持ってくる
            # 6を3に持ってくるとき
            # 6以上の要素ですでに使われているものがあると、swap_cntが増える
            # 使われている数だけ、6が増える
            # 3を6に持ってくるとき
            # 3以上の要素ですでに使われているものがあると、swap_cntが減る・・・
            # 使われている数だけ、3が増える
            S_1 = (1 << (i+1))-1  # i以下の要素のみからなる集合
            S_2 = ~S_1  # iより大の要素のみからなる集合
            S_3 = pre_S & S_2  # iより大かつ既に使われている数
            j = i + popcount(S_3)  # 現在のiの位置
            swap_cnt = abs(num - j)
            cost1 = abs(B[num] - a_i)*x
            cost2 = swap_cnt*y
            cost = DP[pre_S] + cost1 + cost2
            DP[S] = min(DP[S], cost)

    ans = DP[ALL-1]
    print(ans)


def popcount(S):
    return bin(S).count('1')


main()
