# S = 既にゴールしているウサギ
def main():
    n, m = map(int, input().split())
    faster_of = [[] for _ in range(n)]
    for _ in range(m):
        fast, slow = map(lambda x: int(x)-1, input().split())
        faster_of[slow].append(fast)

    # 配るDP
    ALL = 1 << n
    DP = [0] * ALL
    DP[0] = 1
    for cur_S in range(ALL):
        for nex_y in range(n):
            if cur_S >> nex_y & 1:
                continue
            faster_check = True
            for fast_y in faster_of[nex_y]:
                # fast_yがcur_Sに含まれていなければならない
                if cur_S >> fast_y & 1 == 0:
                    faster_check = False
                    break
            if not faster_check:
                continue
            nex_S = cur_S | 1 << nex_y
            DP[nex_S] += DP[cur_S]

    ans = DP[ALL-1]
    print(ans)


main()
