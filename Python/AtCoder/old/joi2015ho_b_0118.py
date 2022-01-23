# [le, ri]をすでに食べた状態で、今まで食べたケーキの量の最大値DP[le][ri]とする
# ケーキは[0, n-1]の範囲である
# DP[le][le-1]はすべて食べた状態であり、ans
# DP[le][le]はleのみ食べた状態
# 食べた数が多いほうから見ていく
import random


def main():
    n = 4
    A = [1, 2, 3, 4]
    while True:
        # random.shuffle(A)
        ret1 = solve1(n, A)
        ret2 = solve2(n, A)
        print(ret1, ret2, n, A)
        if ret1 != ret2:
            break


def solve1(n, A):
    DP = [[0] * n for _ in range(n)]

    for eat_cnt in range(1, n+1):
        for le in range(n):
            ri = (le + eat_cnt - 1) % n
            is_me = ((n-eat_cnt) % 2 == 0)
            # is_me = (eat_cnt % 2 == 1) じゃいけない理由がわからない・・・
            if is_me:
                # 自分のターンの場合
                get_le = A[le] + DP[(le+1) % n][ri]
                get_ri = A[ri] + DP[le][(ri-1) % n]
                DP[le][ri] = max(get_le, get_ri)
            else:
                # 相手は、A[le]とA[ri]のうち大きいほうを食べる
                if A[le] > A[ri]:
                    DP[le][ri] = DP[(le+1) % n][ri]
                else:
                    DP[le][ri] = DP[le][(ri-1) % n]

    ans = -1
    for i in range(n):
        ans = max(ans, DP[i][(i-1) % n])
    return ans


def solve2(n, A):
    DP = [[0] * n for _ in range(n)]

    for eat_cnt in range(n):
        # 配るDP
        for le in range(n):
            ri = (le + eat_cnt - 1) % n
            is_me = (eat_cnt % 2 == 0)
            if is_me:
                # 自分のターンの場合
                DP[(le-1) % n][ri] = max(DP[(le-1) % n][ri], A[le] + DP[le][ri])
                DP[le][(ri+1) % n] = max(DP[le][(ri+1) % n], A[le] + DP[le][ri])
            else:
                # 相手は、A[le]とA[ri]のうち大きいほうを食べる
                if A[le] > A[ri]:
                    DP[(le-1) % n][ri] = DP[le][ri]
                else:
                    DP[le][(ri+1) % n] = DP[le][ri]

    ans = -1
    for i in range(n):
        ans = max(ans, DP[i][(i-1) % n])
    return ans


main()
