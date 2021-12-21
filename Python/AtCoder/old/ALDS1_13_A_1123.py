# 8!=40320通りなので、列についてだけ見ればよい
from itertools import permutations


def main():
    k = int(input())
    # 各行に対して、queenが何列目にいるか
    queen_pos = [-1]*8
    for _ in range(k):
        r, c = map(int, input().split())
        queen_pos[r] = c

    def check(queen_result):
        for r, c in enumerate(queen_result):
            for d in range(-8, 9):
                if d == 0:
                    continue
                cur_r = r + d
                cur_c = c + d
                if not(0 <= cur_r < 8 and 0 <= cur_c < 8):
                    continue
                if queen_result[cur_r] == cur_c:
                    return False
            for d in range(-8, 9):
                if d == 0:
                    continue
                cur_r = r - d
                cur_c = c + d
                if not(0 <= cur_r < 8 and 0 <= cur_c < 8):
                    continue
                if queen_result[cur_r] == cur_c:
                    return False
        return True

    perm = permutations(range(8))
    for p in perm:
        # print(p)
        queen_result = [-1]*8
        for r, c in enumerate(p):
            # 各r行について、queenをc列に置く
            # check1 既に指定されているか
            if queen_pos[r] != -1:
                if queen_pos[r] != c:
                    break
            # check2 置こうとしているところが空いているか
            if queen_result[r] != -1:
                break
            # 採用しうる場合は、queen_resultに追加
            queen_result[r] = c
        if min(queen_result) >= 0:
            # check3 斜めに重複していなかったら、結果を出力
            if check(queen_result):
                # print('test')
                break

    grid = [['.']*8 for _ in range(8)]
    for r, c in enumerate(queen_result):
        grid[r][c] = 'Q'

    for g in grid:
        print(''.join(g))


main()

