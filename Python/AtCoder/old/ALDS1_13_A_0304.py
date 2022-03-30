# バックトラック
# 深さ優先探索
def main():
    k = int(input())
    queen_list = []
    for _ in range(k):
        r, c = map(int, input().split())
        queen_list.append((r, c))

    def nei_of(pre):
        r_set = set()
        c_set = set()
        for r, c in pre:
            r_set.add(r)
            c_set.add(c)
        for r in range(8):
            if r in r_set:
                continue
            for c in range(8):
                if c in c_set:
                    continue
                if (r, c) in pre:
                    continue
                yield pre + [(r, c)]

    def check(cur):
        # 同じ行、同じ列、斜めに重複していないか
        cur_set = set(cur)
        for queen in cur:
            drc_list = [(1, 0), (0, 1), (1, 1), (-1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1)]
            for dcr in drc_list:
                for i in range(1, 9):
                    dr, dc = dcr
                    dr *= i
                    dc *= i
                    moved_queen_r = queen[0] + dr
                    moved_queen_c = queen[1] + dc
                    if not (0 <= moved_queen_r < 8 and 0 <= moved_queen_c < 8):
                        break
                    if (moved_queen_r, moved_queen_c) in cur_set:
                        return False
        return True

    que = [queen_list]
    # nodeとして、今置いているクイーンの座標を保持
    ans = None
    while que:
        pre = que.pop()
        if len(pre) == 8:
            ans = pre
            break
        for cur in nei_of(pre):
            if not check(cur):
                continue
            que.append(cur)

    if ans is None:
        print(-1)
        return
    grid = [['.'] * 8 for _ in range(8)]
    for r, c in ans:
        grid[r][c] = 'Q'
    for row in grid:
        print(''.join(row))


main()
