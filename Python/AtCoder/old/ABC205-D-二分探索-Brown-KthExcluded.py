def main():
    n, q, *t = map(int, open(0).read().split())
    a = t[:n]
    k = t[n:]

    for i in range(q):
        pass
        # 全ての正整数のうち、小さいほうから数えてk[i]番目のものans=k[i]
        # aに含まれるk[i]以下の数の個数d[0]→ans=k[i]+d[0]になる
        # aに含まれるk[i]+d[0]以下の数の個数d[1]→ans=k[i]+d[1]になる
        # 以降、d[n]が変更しなくなるまで続ける
        d = 1e18
        d_pre = 0
        ans = k[i]
        while d != d_pre:
            d_pre = d
            d = count_d(a, ans)
            ans = k[i] + d
        print(ans)


def count_d(a, x):
    # a is sorted
    global memo
    if x in memo:
        return memo[x]
    ok = -1
    ng = len(a)
    while (ng - ok) > 1:
        mid = int((ok + ng)/2)
        if a[mid] <= x:  # midは条件を満たす
            ok = mid
        else:
            ng = mid

    memo[x] = ok + 1
    return ok + 1


memo = {}
main()