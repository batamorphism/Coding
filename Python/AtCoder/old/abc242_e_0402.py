MOD = 998244353


def main():
    t = int(input())
    ans_list = []
    for _ in range(t):
        n = int(input())
        S = input()
        ans = solve(n, S)
        ans_list.append(ans)
    print(*ans_list, sep='\n')


def solve(n, S):
    A = [c2i(c) for c in S]
    # n=1 -> m = 1
    # n=2 -> m = 1
    # n=3 -> m = 2
    m = (n+2-1) // 2
    K = [0] * n  # 回文
    for i in range(m):
        K[i] = A[i]
        K[n-i-1] = A[i]

    # 題意を満たす最大の回文を作成する
    if K > A:
        # Kを一個小さくする
        if n % 2 == 0:
            K[m-1] -= 1
            K[m] -= 1
        else:
            K[m-1] -= 1

    # K以下の配列が何通りあるか
    H = K[:m]

    ans = 0
    for i in range(m):
        # 1. 既に確定しているものの末尾にA~Zを追加する
        ans *= 26
        # 2. H[:i]から始まる文字を追加する
        ans += H[i]
        ans %= MOD
    ans += 1
    ans %= MOD
    return ans


def c2i(c):
    return ord(c) - ord('A')


main()
