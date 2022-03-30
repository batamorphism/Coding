from collections import defaultdict


def main():
    S = input()
    n = len(S)
    DP = [0]*(n+1)
    DP_SUM = [0]*(n+1)
    DP[0] = 1
    DP_SUM[0] = 1

    bef_pos_of = defaultdict(lambda: -1)
    for i, s_i in enumerate(S, 1):
        bef_pos = bef_pos_of[s_i]
        if bef_pos == -1:
            DP[i] += DP_SUM[i-1]
        else:
            DP[i] += DP_SUM[i-1] - DP_SUM[bef_pos-1]
        DP_SUM[i] += DP[i] + DP_SUM[i-1]
        bef_pos_of[s_i] = i

    ans = sum(DP)
    print(ans)


main()
