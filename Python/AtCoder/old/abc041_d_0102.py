# bit = 既にゴールしているウサギ
def main():
    node_end, m = map(int, input().split())
    x_of = [[] for _ in range(node_end)]
    for _ in range(m):
        x, y = map(lambda x: int(x)-1, input().split())
        x_of[y].append(x)

    ALL = 1 << node_end
    DP = [0] * ALL
    DP[0] = 1
    for S in range(ALL):
        for y in range(node_end):
            # S / {y}
            if S & (1 << y) == 0:
                continue
            pre_S = S ^ (1 << y)
            # x_of[y] is subset of pre_S
            is_subset = True
            for x in x_of[y]:
                if not pre_S & (1 << x):  # x in pre_S
                    is_subset = False
            if is_subset:
                DP[S] += DP[pre_S]
            else:
                DP[S] = 0

    ans = DP[ALL-1]
    # print(DP)
    print(ans)


main()
