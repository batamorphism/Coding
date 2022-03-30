# 全探索して、足りないマスの数が2以下であればよい
def main():
    n = int(input())
    grid = [input() for _ in range(n)]

    INF = float('inf')
    for r in range(n):
        for c in range(n):
            max_cnt = 0  # #となっているマスの数の最大値
            # 右側
            cnt = 0
            for dr in range(6):
                cur_r = r+dr
                cur_c = c
                if not (0 <= cur_r < n and 0 <= cur_c < n):
                    cnt = -INF
                    break
                if grid[cur_r][cur_c] == '#':
                    cnt += 1
            max_cnt = max(max_cnt, cnt)
            # 左側
            cnt = 0
            for dr in range(6):
                cur_r = r-dr
                cur_c = c
                if not (0 <= cur_r < n and 0 <= cur_c < n):
                    cnt = -INF
                    break
                if grid[cur_r][cur_c] == '#':
                    cnt += 1
            max_cnt = max(max_cnt, cnt)
            # 下側
            cnt = 0
            for dc in range(6):
                cur_r = r
                cur_c = c+dc
                if not (0 <= cur_r < n and 0 <= cur_c < n):
                    cnt = -INF
                    break
                if grid[cur_r][cur_c] == '#':
                    cnt += 1
            max_cnt = max(max_cnt, cnt)
            # 上側
            cnt = 0
            for dc in range(6):
                cur_r = r
                cur_c = c-dc
                if not (0 <= cur_r < n and 0 <= cur_c < n):
                    cnt = -INF
                    break
                if grid[cur_r][cur_c] == '#':
                    cnt += 1
            max_cnt = max(max_cnt, cnt)
            # 右斜め下
            cnt = 0
            for drc in range(6):
                cur_r = r+drc
                cur_c = c+drc
                if not (0 <= cur_r < n and 0 <= cur_c < n):
                    cnt = -INF
                    break
                if grid[cur_r][cur_c] == '#':
                    cnt += 1
            max_cnt = max(max_cnt, cnt)
            # 斜め2
            cnt = 0
            for drc in range(6):
                cur_r = r-drc
                cur_c = c+drc
                if not (0 <= cur_r < n and 0 <= cur_c < n):
                    cnt = -INF
                    break
                if grid[cur_r][cur_c] == '#':
                    cnt += 1
            max_cnt = max(max_cnt, cnt)
            # 斜め3
            cnt = 0
            for drc in range(6):
                cur_r = r+drc
                cur_c = c-drc
                if not (0 <= cur_r < n and 0 <= cur_c < n):
                    cnt = -INF
                    break
                if grid[cur_r][cur_c] == '#':
                    cnt += 1
            max_cnt = max(max_cnt, cnt)
            # 斜め4
            cnt = 0
            for drc in range(6):
                cur_r = r-drc
                cur_c = c-drc
                if not (0 <= cur_r < n and 0 <= cur_c < n):
                    cnt = -INF
                    break
                if grid[cur_r][cur_c] == '#':
                    cnt += 1
            max_cnt = max(max_cnt, cnt)
            if max_cnt >= 4:
                print('Yes')
                return
    print('No')


main()
