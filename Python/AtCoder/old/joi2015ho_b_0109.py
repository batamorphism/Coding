# 区間DP
# DP[le][ri] := [le, ri)が残った状態で、そこから追加で取れる分
def main():
    n = int(input())
    A = [int(input()) for _ in range(n)]

    DP = [[0] * n for _ in range(n)]

    for remain_cnt in range(1, n+1):
        # ケーキが残っている数が少ないほうから見ていく
        for le in range(n):
            # ri - le = removed_cnt
            removed_cnt = n - remain_cnt
            ri = (remain_cnt + le) % n
            is_my_turn = (removed_cnt % 2 == 0)

            if is_my_turn:
                get_le = DP[(le + 1) % n][ri] + A[le]
                get_ri = DP[le][(ri - 1) % n] + A[ri-1]
                DP[le][ri] = max(get_le, get_ri)
            else:
                if A[le] > A[ri-1]:
                    DP[le][ri] = DP[(le + 1) % n][ri]
                else:
                    DP[le][ri] = DP[le][(ri - 1) % n]

    ans = 0
    for i in range(n):
        ans = max(ans, DP[i][i])

    print(ans)


main()
