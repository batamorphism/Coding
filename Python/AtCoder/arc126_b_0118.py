# 転倒数が0となるように
# 最長増加部分列
# 初めにaでソートしておく
# bが小さいほうが良い
# p = (a, b)について
# p1 < p2 <->  a1 < a2 ただしa1==a2のときばb1 > b2とする
# pの最長増加部分列を求める
def main():
    n, m = map(int, input().split())
    p_list = []
    for _ in range(m):
        a, b = map(int, input().split())
        p_list.append((a, b))

    # aは昇順、bは降順でソート
    p_list.sort(key=lambda x: (x[0], -x[1]))
    B = [p[1] for p in p_list]
    ans = lis(B)
    print(ans)


def lis(A):
    # Aの狭義単調増加となる部分列の長さの最大値
    n = len(A)
    INF = float('inf')
    DP = [INF]*(n+1)
    DP[0] = -INF
    ans = -1
    for a in A:
        # DP[i] < aとなる最大のiを求め
        # DP[i+1] = aとする
        ok = 0
        ng = n
        while ng - ok > 1:
            mid = (ok+ng)//2
            if DP[mid] < a:
                ok = mid
            else:
                ng = mid
        DP[ok+1] = a
        ans = max(ans, ok+1)
    return ans


main()
