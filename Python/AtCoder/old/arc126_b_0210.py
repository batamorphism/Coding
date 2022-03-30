# 最長増加部分列
# a順にソートしたbについて、最長増加部分列を求める
# aが同じ場合は、bが小さいほうが有利なので、逆順にソート
def main():
    n, m = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(m)]
    AB.sort(key=lambda x: (x[0], -x[1]))

    # Bの最長増加部分列を求める
    B = [x[1] for x in AB]
    ans = lcs(B)
    print(ans)


def lcs(A):
    # Aの最長増加部分
    n = len(A)
    INF = float('inf')
    DP = [INF]*(n+1)
    DP[0] = -INF
    ans = -INF

    for a_i in A:
        ok = 0
        ng = n+1
        while ng - ok > 1:
            mid = (ok+ng)//2
            if DP[mid] < a_i:
                ok = mid
            else:
                ng = mid
        DP[ok+1] = a_i
        ans = max(ans, ok+1)
    return ans


main()
