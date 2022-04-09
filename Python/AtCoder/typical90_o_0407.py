MOD = 10**9+7
n_end = 10**5+1
factorial = [1]*n_end
rev_factorial = [1]*n_end


def rev(val):
    return pow(val, MOD-2, MOD)


def nCr(n, r):
    return factorial[n]*rev_factorial[r]*rev_factorial[n-r]


def nHr(n, r):
    return nCr(n+r-1, r)


for i in range(1, n_end):
    factorial[i] = factorial[i-1]*i % MOD
    rev_factorial[i] = rev(factorial[i])


def main():
    n = int(input())
    for k in range(1, n+1):
        print(solve(n, k))


def solve(n, k):
    # 1, ...,nを
    # 書かれている整数の差がk以上となるようにいくつか選ぶ
    # 選んだ個数をcntとする
    ans = 0
    for cnt in range(1, n+1):
        if k*cnt > n+(k-1):
            break
        # これは、幅kの区間を1,...,nに埋め込む(はみ出してもよい)のと相当する
        # n-k*cnt個の、使われないボールが出てくる
        # ここで、右端にボールを置くと、(k-1)個だけはみ出るので、
        # 使われないボールをk-1個かさましする。(n-k*cnt+(k-1))
        # 使われないボールの間（両端含む）のn-k*cnt+(k-1)+1箇所に
        # cnt個を重複組み合わせで選べばよい
        ans += nHr(n-k*cnt+1+(k-1), cnt)
        ans %= MOD
    return ans


main()
