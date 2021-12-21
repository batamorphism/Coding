mod = 10**9 + 7

def main():
    n, q = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    C = [1] + list(map(int, input().split())) + [1]
    # 累積和は1-indexed
    # D[i] := A[i-1] -> A[i]のコスト
    # ただしD[0] = 0
    # c_lo -> c_hiのコストはD[lo+1]+...+D[hi]なので
    # SUM[hi] - SUM[lo]

    D = [0]*(n+1)
    for i in range(2, n+1):
        D[i] = pow(A[i-1], A[i], mod)

    for i in range(1, n+1):
        D[i] = (D[i] + D[i-1]) % mod

    ans = 0
    for i, c_i in enumerate(C[:-1]):
        j = i+1
        c_j = C[j]
        hi, lo = max(c_i, c_j), min(c_i, c_j)
        d = D[hi] - D[lo]
        ans += d
        ans %= mod

    print(ans)


main()
