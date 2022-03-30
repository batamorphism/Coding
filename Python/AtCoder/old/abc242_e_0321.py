MOD = 998244353


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        S = input()
        solve(n, S)


def solve(n, S):
    A = [c2i(c) for c in S]
    kaibun = [-1]*n
    mid = (n+1)//2  # 0～midまでを反転させる
    for i in range(mid):
        a_i = A[i]
        kaibun[i] = a_i
        kaibun[n-i-1] = a_i

    # kaibun以下について考える
    ans = 0
    for i in range(mid):
        ans *= 26  # 既に確定している文字列の末尾にA~Zを追加
        ans += kaibun[i]  # 新たな文字列を追加
        ans %= MOD
    ans += 1  # kaibunそのもの
    if kaibun > A:
        ans -= 1
    ans %= MOD
    print(ans)


def c2i(c):
    return ord(c) - ord('A')


main()
