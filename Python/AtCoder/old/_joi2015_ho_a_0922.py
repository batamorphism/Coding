def main():
    n, m = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(m):
        P[i] -= 1
    A = [0]*n
    B = [0]*n
    C = [0]*n
    for i in range(n-1):
        a, b, c = map(int, input().split())
        A[i] = a
        B[i] = b
        C[i] = c

    imos = [0]*n

    for i in range(m-1):
        # P[i]->P[i+1]の順に旅をする
        # P[i]とP[i+1]のうち小さいほうで+1、大きいほうで-1
        if P[i] < P[i+1]:
            imos[P[i]] += 1
            imos[P[i+1]] -= 1
        else:
            imos[P[i]] -= 1
            imos[P[i+1]] += 1

    railway_cnt = [0]*(n-1)

    now_cnt = 0
    for i in range(n-1):
        now_cnt += imos[i]
        railway_cnt[i] = now_cnt

    ans = 0
    for i in range(n-1):
        ans += cost(i, railway_cnt, A, B, C)

    print(ans)


def cost(i, railway_cnt, A, B, C):
    return min(railway_cnt[i]*A[i], railway_cnt[i]*B[i]+C[i])


main()
