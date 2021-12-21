from collections import deque


# DP[i][val]
# i日目にaかbかを選択した場合の、総額がvalになるパターンが存在するか?
def main():
    # 配るDPは0-indexed
    n_end, s = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(n_end)]

    DP = [[0]*(s+1) for _ in range(n_end+1)]
    bef = [[('', 0)]*(s+1) for _ in range(n_end+1)]
    DP[0][0] = 1
    for i, ab in enumerate(AB):
        a, b = ab
        for val in range(s+1):
            if DP[i][val]:
                if val+a <= s:
                    DP[i+1][val+a] = 1
                    bef[i+1][val+a] = ('A', i, val)
                if val+b <= s:
                    DP[i+1][val+b] = 1
                    bef[i+1][val+b] = ('B', i, val)

    is_possible = DP[n_end][s]
    if not is_possible:
        print('Impossible')
        return

    # DP復元
    ans_list = deque()
    i, val = n_end, s
    while i > 0:
        a_or_b, i, val = bef[i][val]
        ans_list.appendleft(a_or_b)

    print(''.join(ans_list))


main()
