INF = 10**12


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    A.sort()
    q = int(input())
    ans = []
    for _ in range(q):
        b = int(input())
        # bisect
        lo = bisect_left(A, b)
        hi = bisect_right(A, b)
        ans.append(min(abs(b-lo), abs(b-hi)))

    print(*ans)


def bisect_left(A: list, x: int):
    # Aの要素のうち、A[i] <= x となる最大のA[i]を返す
    # ただし存在しないときは、-INF
    ok = -1
    ng = len(A)
    while ng-ok > 1:
        mid = (ok+ng)//2
        if A[mid] <= x:
            ok = mid
        else:
            ng = mid
    if ok == -1:
        return -INF
    return A[ok]


def bisect_right(A: list, x: int):
    # Aの要素のうち、A[i] >= x となる最小のA[i]を返す
    # ただし存在しないときは、INF
    ok = len(A)
    ng = -1
    while ok-ng > 1:
        mid = (ok+ng)//2
        if A[mid] >= x:
            ok = mid
        else:
            ng = mid
    if ok == len(A):
        return INF
    return A[ok]


main()
