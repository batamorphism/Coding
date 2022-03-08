from collections import defaultdict


def main():
    S = input()
    n = len(S)
    bef_of = defaultdict(lambda: -1)
    DP = [0] * (n+1)
    DP[0] = 1

    for i, c_i in enumerate(S, 1):
        bef_i = bef_of[c_i]
        if bef_i == -1:
            # 初登場
            dp = sum(DP[:i])  # 今まで登場した文字の末尾にc_iを追加
        else:
            dp = sum(DP[bef_i:i])
        DP[i] = dp
        bef_of[c_i] = i

    ans = sum(DP)
    print(ans)


main()
