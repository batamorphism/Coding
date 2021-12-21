from itertools import permutations
from collections import Counter


# 全探索いける
# 0-7から1つずつ8個選ぶ
def main():
    n = int(input())
    prefix_queen_set = set([tuple(map(int, input().split())) for _ in range(n)])
    for perm in permutations(range(8)):
        # queenのいる場所を座標で与える
        queen_set = set()
        for r, c in enumerate(perm):
            queen_set.add((r, c))
        if not prefix_queen_set.issubset(queen_set):
            continue

        if check(queen_set):
            ans = make_grid(queen_set)
            for row in ans:
                print(''.join(row))


def check(queen_list):
    # 各queenが縦横斜めに同じ座標の者がないことを確認する
    # 斜めだけ確認すればよい
    # 45度回転して、縦横に同じ座標のものがあるか確認する
    rotate_queen_list = []
    for r, c in queen_list:
        # 1, 0 -> 1, -1
        # 1, 1 -> 2, 0
        rotate_queen_list.append((r+c, -r+c))

    r_cnt = Counter()
    c_cnt = Counter()
    for r, c in rotate_queen_list:
        r_cnt[r] += 1
        c_cnt[c] += 1
    if max(r_cnt.values()) > 1 or max(c_cnt.values()) > 1:
        return False
    else:
        return True


def make_grid(queen_list):
    ans = [['.']*8 for _ in range(8)]
    for r, c in queen_list:
        ans[r][c] = 'Q'
    return ans


main()
