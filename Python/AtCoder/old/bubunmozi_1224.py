from collections import defaultdict


def main():
    S = '*' + input()
    n = len(S)
    # DP[i] = i文字目を必ず使うとした場合の部分文字列の個数
    # ただし、すでに出てきている部分文字列は除外する
    # dpは1-indexed
    # DP[0] = 1 <- 空文字''分
    # s_i = S[i]
    # 重複を考えなければ、DP[i] = sum(DP[0],...,DP[i-1])
    # 直前にs_iが出てきたインデックスをjとして
    # DP[i]はDP[j]までの分だけ重複する、すなわち、
    # abcxefgx を考えたとき、最後のxを足して新たに作られる部分文字列の個数は
    # abcxまで見て作られる部分文字列の個数分重複し、efgを使った分だけが新たにカウントされる
    # DP[i] = sum(DP[j+1],...,DP[i-1])
    DP = [0] * n
    DP[0] = 1
    d = defaultdict(int)

    for i, s_i in enumerate(S[1:], 1):
        j = d[s_i]
        dp = 0
        # 実際はBITとかで高速化する
        for k in range(j, i):
            dp += DP[k]
        DP[i] = dp
        d[s_i] = i

    ans = sum(DP)
    print(ans)


main()
