mod = 1000000007


def main():
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    C = [c-1 for c in C]
    C = [0] + C + [0]
    # dist[i]: 都市0からiの距離
    dist = [0]*n
    for i in range(n):
        if i == 0:
            dist[i] = 0
            continue
        dist[i] = dist[i-1] + pow(A[i-1], A[i], mod)
        dist[i] %= mod

    ans = 0
    for i in range(len(C)-1):
        fr = C[i]
        to = C[i+1]
        if fr <= to:
            ans += dist[to]-dist[fr]
        else:
            ans += dist[fr]-dist[to]
        ans %= mod
    print(ans)


main()
