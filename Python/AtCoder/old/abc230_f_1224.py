from collections import defaultdict
mod = 998244353


def main():
    _ = int(input())
    A = [0] + list(map(int, input().split()))
    n = len(A)
    # 累積和
    for i in range(1, n):
        A[i] += A[i-1]

    # 座圧
    A_zipper = {a: i for i, a in enumerate(sorted(set(A)))}
    A = [A_zipper[a] for a in A]

    # setup bit
    bit_end = n + 10
    bit_dat = [0]*bit_end

    def add(pos, val):
        pos += 1
        while pos < bit_end:
            bit_dat[pos] += val
            pos += (pos & -pos)

    def getsum(pos):
        pos += 1
        ret = 0
        while pos > 0:
            ret += bit_dat[pos]
            pos -= (pos & -pos)
        return ret

    # DP[i] = i文字目を必ず使うとした場合の部分列の個数
    # ただし、すでに出てきている部分文字列は除外する
    # dpは1-indexed
    # DP[0] = 1 <- 空列[]分
    # s_i = S[i]
    # 重複を考えなければ、DP[i] = sum(DP[0],...,DP[i-1])
    # 直前にs_iが出てきたインデックスをjとして
    # DP[i]はDP[j]までの分だけ重複する、すなわち、
    # abcxefgx を考えたとき、最後のxを足して新たに作られる部分文字列の個数は
    # abcxまで見て作られる部分文字列の個数分重複し、efgを使った分だけが新たにカウントされる
    # DP[i] = sum(DP[j+1],...,DP[i-1])
    d = defaultdict(int)

    """
    DP = [0] * n
    DP[0] = 1
    """
    add(0, 1)
    ans = 0
    a_last = A[-1]
    for i, a_i in enumerate(A[1:], 1):
        j = d[a_i]
        dp = getsum(i-1) - getsum(j-1)
        dp %= mod
        """
        for k in range(j, i):
            dp += DP[k]
        DP[i] = dp
        """
        add(i, dp)
        if a_i == a_last:
            # a_lastと同じ場合
            # この部分列は、元のAの全体に対して和を取ったものとなる
            # したがって、答えに加算する
            ans += dp
            ans %= mod
        d[a_i] = i

    print(ans)


main()
