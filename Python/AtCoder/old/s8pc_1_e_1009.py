def main():
    mod = 1000000007
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A = [0] + A
    C.append(1)
    C = [1] + C
    DATA = [0]*(n+1)

    def dist_of(i, j):
        # iからjまでの距離
        ma = max(i, j)
        mi = min(i, j)
        return (get_sum(ma)-get_sum(mi)) % mod

    def get_sum(pos):
        return DATA[pos]

    for i in range(0, n):
        cost = pow(A[i], A[i+1], mod)
        DATA[i+1] = (DATA[i]+cost) % mod

    cost = 0
    for i in range(q+1):
        fr = C[i]
        to = C[i+1]
        cost += dist_of(fr, to)
        cost %= mod

    print(cost)


main()
