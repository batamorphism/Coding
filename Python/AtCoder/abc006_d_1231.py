def main():
    # 最長増加部分列の長さを求める
    n = int(input())
    C = [int(input()) for _ in range(n)]
    # DPは1-indexed
    n_end = n + 1

    INF = float('inf')
    DP = [INF] * n_end
    DP[0] = -INF
    ans = -INF

    # DP[i] := 最長増加部分列の要素i
    for c in C:
        for i in range(1, n_end):
            # bisect
            ng = 0
            ok = n_end
            while ok - ng > 1:
                mid = (ok + ng)//2
                if DP[mid] > c:
                    ok = mid
                else:
                    ng = mid
            DP[ok] = c
            ans = max(ans, ok)
            break
            """
            if DP[i] > c:
                DP[i] = c
                print(i, c)
                ans = max(ans, i)
                break
            """

    # print(DP)
    ans = n - ans
    print(ans)


main()
