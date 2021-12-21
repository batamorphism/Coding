def main():
    n = int(input())
    A = [int(input()) for _ in range(n)]

    # A[0]が0であり、Aが増えるときの増加幅が1であるときに限り、作成可能
    if A[0] != 0:
        print(-1)
        return
    for i in range(1, n):
        if A[i] > A[i-1]:
            if A[i]-A[i-1] != 1:
                print(-1)
                return

    # したがって、Aは増えるときは増加幅1で、それ以外は維持か減るか
    # 増加の時は加算なし、
    # 維持か減るかの時はaを加算
    ans = 0
    for i in range(n):
        if i == n-1:
            ans += A[i]
            continue
        if A[i] >= A[i+1]:
            ans += A[i]
    print(ans)


main()
