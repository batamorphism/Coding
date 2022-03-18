def main():
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    C = [0] + list(map(lambda x: int(x)-1, input().split())) + [0]
    MOD = 10**9 + 7

    # 0からiの距離をdist[i]とする
    dist = [0]*n
    for i in range(1, n):
        # a_(i-1)とa_iを結ぶ道路の長さはa_(i-1)**a_iである
        cost = pow(A[i-1], A[i], MOD)
        dist[i] = (dist[i-1] + cost) % MOD

    ans = 0
    for pre_i, pre_node in enumerate(C[:-1]):
        cur_i = pre_i + 1
        cur_node = C[cur_i]
        if cur_node >= pre_node:
            ans += dist[cur_node]-dist[pre_node]
        else:
            ans -= dist[cur_node]-dist[pre_node]
        ans %= MOD

    print(ans)


main()
