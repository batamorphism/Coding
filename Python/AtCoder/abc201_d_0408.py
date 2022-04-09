# ミニマックス法
# 各状態の評価値を決めておいて
# 先手は、評価値が大きくなるように行動
# 後手は、評価値が小さくなるように行動

# 評価値は、その場所にいる時点で、そのあと互いが最適な行動をとった場合における
# 最終的な得点とする
def main():
    r_end, c_end = map(int, input().split())
    grid = []
    for _ in range(r_end):
        row = list(input())
        row = [c2score(c) for c in row]
        grid.append(row)

    INF = float('inf')
    score_of = [[None]*c_end for _ in range(r_end)]
    score_of[-1][-1] = 0

    def nei_of(cur_r, cur_c):
        drc = [(1, 0), (0, 1)]
        for dr, dc in drc:
            nex_r = cur_r+dr
            nex_c = cur_c+dc
            if not (0 <= nex_r < r_end and 0 <= nex_c < c_end):
                continue
            yield nex_r, nex_c

    for cur_r in reversed(range(r_end)):
        for cur_c in reversed(range(c_end)):
            if cur_r == r_end-1 and cur_c == c_end-1:
                continue
            is_first = (cur_r+cur_c) % 2 == 0
            if is_first:
                # 先手番は高橋君
                # スコアが大きくなるように行動する
                score = -INF
                for nex_r, nex_c in nei_of(cur_r, cur_c):
                    score = max(score, score_of[nex_r][nex_c] + grid[nex_r][nex_c])
                score_of[cur_r][cur_c] = score
            else:
                # スコアが小さくなるように行動する
                score = INF
                for nex_r, nex_c in nei_of(cur_r, cur_c):
                    score = min(score, score_of[nex_r][nex_c] - grid[nex_r][nex_c])
                score_of[cur_r][cur_c] = score
    score = score_of[0][0]
    if score > 0:
        print('Takahashi')
    elif score == 0:
        print('Draw')
    else:
        print('Aoki')


def c2score(c):
    if c == '+':
        return 1
    else:
        return -1


main()
