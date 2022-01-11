from collections import defaultdict


def main():
    n, m = map(int, input().split())
    prop_of = defaultdict(list)
    for _ in range(m):
        x, y, z = map(int, input().split())
        prop_of[x].append((y, z))

    ALL = 1 << n
    DP = [0] * ALL
    DP[0] = 1  # 空集合は1
    for cur_S in range(1, ALL):
        cur_n = popcount(cur_S)

        # check prop
        prop_list = prop_of[cur_n]
        is_ok = True
        for prop in prop_list:
            y, z = prop
            # cur_Sに、y以下の要素がz個以下か
            S_and_y = cur_S & ((1 << y) - 1)
            if popcount(S_and_y) > z:
                is_ok = False
                break
        if not is_ok:
            continue

        dp = 0
        for a in range(n):
            if not have(cur_S, a):
                continue
            pre_S = cur_S ^ (1 << a)
            # pre_Sにaを足すとcur_Sになる
            dp += DP[pre_S]
        DP[cur_S] = dp

    ans = DP[ALL-1]
    print(ans)


def popcount(S):
    return bin(S).count('1')


def have(S, a):
    # Sにaが含まれているか
    return (S >> a) & 1


main()
