from functools import lru_cache
import string


def main():
    INF = float('inf')

    n = int(input())
    S = '*' + input()

    # DP[i] = i番目の文字は必ず使うものとして
    # Sのうち0～i番目までの部分から得られる部分文字列の個数
    DP = [0] * (n + 1)
    DP[0] = 1  # ''に対応

    # next[i][c] = Sのi文字目以降で最初に文字cが登場する位置
    # 存在しないときはINF
    @lru_cache(maxsize=None)
    def next_of(i, c):
        if i > n:
            return INF
        if S[i] == c:
            return i
        return next_of(i+1, c)

    # 配るDP
    for i in range(n+1):
        for char in string.ascii_lowercase:
            nex = next_of(i+1, char)
            if nex != INF:
                DP[nex] += DP[i]

    ans = sum(DP)
    print(ans)


main()
