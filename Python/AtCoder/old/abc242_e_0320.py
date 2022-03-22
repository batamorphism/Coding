MOD = 998244353


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        S = input()
        solve(n, S)


def solve(n, S):
    ans = 0
    A = [c2i(c) for c in S]

    mid = (n-1)//2
    # 1 0
    # 2 9
    # 3 1
    # 回文を作る
    kaibun_max = [-1]*n
    for i in range(mid+1):
        kaibun_max[i] = A[i]
        kaibun_max[n-i-1] = A[i]
        ans *= 26  # 既に確定した文字列の末尾にA~Zを追加
        ans += A[i]  # A[i]未満のやつ
        ans %= MOD
    ans += 1
    if kaibun_max > A:
        ans -= 1
    ans %= MOD
    print(ans)


def c2i(c):
    return ord(c) - ord('A')


main()
