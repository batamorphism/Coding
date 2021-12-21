# 半分全列挙
def main():
    n, k, p = map(int, input().split())
    A = list(map(int, input().split()))
    n1 = n // 2
    n2 = n - n1
    A1 = A[:n1]
    A2 = A[n1:]

    plist_of1 = [[] for _ in range(n+1)]
    plist_of2 = [[] for _ in range(n+1)]

    set_plist_of(A1, plist_of1)
    set_plist_of(A2, plist_of2)

    ans = 0
    for k1 in range(k + 1):
        k2 = k - k1
        plist1 = plist_of1[k1]
        plist2 = plist_of2[k2]
        # plist1, plist2の組み合わせのうち、合計がpを下回る個数
        for p1 in plist1:
            cnt = bisect(plist2, p - p1)
            ans += cnt
    print(ans)


def set_plist_of(A, plist_of):
    # Aからk個選んだ時の、それらの要素の和のリストを作る
    n = len(A)
    all = 1 << n
    for bit in range(all):
        val = 0
        k = 0
        for i, a in enumerate(A):
            if bit & (1 << i):
                val += a
                k += 1
        plist_of[k].append(val)

    for plist in plist_of:
        plist.sort()


def bisect(A, x):
    # Aのうちx以下の要素の個数を返す
    ok = -1
    ng = len(A)
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if A[mid] <= x:
            ok = mid
        else:
            ng = mid
    return ok + 1


main()
