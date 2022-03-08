def main():
    n = int(input())
    S = list(map(int, input().split()))
    q = int(input())
    T = list(map(int, input().split()))

    S.sort()
    T.sort()

    ans = 0
    for t in T:
        val = lower_bound(S, t)
        if val == t:
            ans += 1
    print(ans)


def lower_bound(array, val):
    return array[bisect_le(array, val)]


def bisect_le(array, val):
    ok = 0
    ng = len(array)
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if array[mid] <= val:
            ok = mid
        else:
            ng = mid
    return ok


main()
