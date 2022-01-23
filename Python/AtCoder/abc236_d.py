import sys
sys.setrecursionlimit(10**6)

ans = -1
# ペアの作り方を全探索
# Pairs[a] = b := aとbがペアとなる
def main():
    n = int(input())
    n *= 2

    ALL = 1 << n
    A = [list(map(int, input().split())) for _ in range(n-1)]

    def calc_ans(pairs):
        global ans
        cur_ans = 0
        for a, b in pairs:
            # a < b
            cur_ans ^= A[a][b-a-1]
        ans = max(ans, cur_ans)

    def dfs(pre_S, pairs):
        # pre_S := 既にペアになった人
        # pairs := ペア(タプル)のリスト
        if pre_S == ALL-1:
            # 全ての人がペアとなった
            calc_ans(pairs)
            return
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
                if cur1 == cur2:
                    continue
                pairs.append((cur1, cur2))
                cur_S = pre_S | (1 << cur1) | (1 << cur2)
                dfs(cur_S, pairs)
                pairs.pop()

    dfs(0, [])

    print(ans)


main()
