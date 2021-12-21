# 各生徒のレーティングbに対し、それ以下で最も高いクラスa_loとそれ以上で最も低いクラスa_hiを求める。
INF = 10**12


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    B = [int(input()) for _ in range(q)]

    AB = []
    for a in A:
        AB.append((a, 'A'))
    for b in B:
        AB.append((b, 'B'))

    AB.sort()
    # print(AB)

    Lo = []
    a_lo = -INF
    for ab in AB:
        val, cls = ab
        if cls == 'A':
            a_lo = val
        else:
            Lo.append(a_lo)

    Hi = []
    a_hi = INF
    for ab in reversed(AB):
        val, cls = ab
        if cls == 'A':
            a_hi = val
        else:
            Hi.append(a_hi)
    Hi.reverse()

    B_sort = [(b, i) for i, b in enumerate(B)]
    B_sort.sort()
    ans = [0]*q

    for bi, a_lo, a_hi in zip(B_sort, Lo, Hi):
        b, i = bi
        cost1 = abs(b - a_lo)
        cost2 = abs(b - a_hi)
        cost = min(cost1, cost2)
        # print(b, a_lo, a_hi, i, cost)
        ans[i] = cost

    print(*ans)


main()
