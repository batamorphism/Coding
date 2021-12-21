def main():
    n, L = map(int, input().split())
    k = int(input())
    A = list(map(int, input().split()))
    A = A+[L]
    B = [0]*(n+1)
    for i in range(n+1):
        if i == 0:
            B[i] = A[i]
            continue
        B[i] = A[i]-A[i-1]

    def check(mid):
        # 長さmidで切り分けていって、k個を超えるか
        c = 0
        cnt = 0
        for b in B:
            c += b
            if c >= mid:
                c = 0
                cnt += 1
        return cnt > k

    ok = 0
    ng = L+1
    while ng-ok > 1:
        mid = (ok+ng)//2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


main()
