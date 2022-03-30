from collections import defaultdict


def main():
    S = input()
    n = len(S)

    DP = [0]*(n+1)
    bef = defaultdict(int)
    DP[0] = 1

    for i in range(1, n+1):
        s_i = S[i-1]
        bef_i = bef[s_i]
        if bef_i == 0:
            DP[i] = sum(DP[:i])
        else:
            DP[i] = sum(DP[bef_i:])
        bef[s_i] = i

    ans = sum(DP)
    print(ans)


main()
