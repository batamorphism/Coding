def main():
    n = int(input())
    S = list(map(int, input().split()))
    q = int(input())
    T = list(map(int, input().split()))

    ans = 0
    for t in T:
        have = bisect(S, t)
        if have:
            ans += 1

    print(ans)


def bisect(S, t):
    # S[i] == tとなるiを探す
    # 存在しなければFalse
    ok = -1
    ng = len(S)
    while ng-ok > 1:
        mid = (ok+ng)//2
        if S[mid] <= t:
            ok = mid
        else:
            ng = mid

    if ok == -1:
        return -1
    return S[ok] == t


main()
