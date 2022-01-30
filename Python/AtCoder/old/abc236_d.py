import sys
sys.setrecursionlimit(10**6)


# ペアの作り方を全探索
# Pairs[a] = b := aとbがペアとなる
def main():
    n = int(input())
    n *= 2

    ALL = 1 << n
    # A = [list(map(int, input().split())) for _ in range(n-1)]

    def calc_val(pairs):
        return 0
        """
        cur_ans = 0
        for a, b in pairs:
            # a < b
            cur_ans ^= A[a][b-a-1]
        return cur_ans
        """

    def dfs(pre_S, pairs):
        # pre_S := 既にペアになった人
        # pairs := ペア(タプル)のリスト
        if pre_S == ALL-1:
            # 全ての人がペアとなった
            yield pairs
        for cur1 in range(n):
            if pre_S >> cur1 & 1:
                # 既にペアがいる
                continue
            # cur1は昇順としてよい
            if ~pre_S & ((1 << cur1) - 1):
                continue
            for cur2 in range(cur1+1, n):
                if pre_S >> cur2 & 1:
                    continue
                pairs.append((cur1, cur2))
                yield from dfs(pre_S | (1 << cur1) | (1 << cur2), pairs)
                pairs.pop()

    ans = -1
    for pairs in dfs(0, []):
        ans = max(ans, calc_val(pairs))

    print(ans)


main()
