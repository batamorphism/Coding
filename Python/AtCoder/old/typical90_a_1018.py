def check(x, A, k):
    cnt = 0
    cur_len = 0
    for a in A:
        if (cur_len + a) >= x:
            # 切り分ける
            cnt += 1
            cur_len = 0
        else:
            cur_len += a
        if cnt > k:
            return True
    return False


def main():
    n, w = map(int, input().split())
    k = int(input())
    A = list(map(int, input().split()))
    A += [w]
    B = []
    for i in range(n+1):
        if i == 0:
            B.append(A[i])
            continue
        B.append(A[i]-A[i-1])
    # Aをk+1個に分割した時の、最も短いものの長さがx以上か
    ok = 0
    ng = w+1
    while ng-ok > 1:
        mid = (ok+ng)//2
        if check(mid, B, k):
            ok = mid
        else:
            ng = mid

    print(ok)


main()
