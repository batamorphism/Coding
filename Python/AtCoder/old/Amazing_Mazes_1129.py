from collections import deque


# 幅優先探索
def main():
    while True:
        w, h = map(int, input().split())
        r_end = 2*h-1
        c_end = 2*w-1
        if w == 0 and h == 0:
            return
        grid = [input() for _ in range(r_end)]
        solver(grid, h, w)


def solver(grid, r_end, c_end):
    st_node = (0, 0)
    dist = [[float('inf')]*c_end for _ in range(r_end)]

    def neighbors(pre):
        pre_r, pre_c = pre
        grid_r, grid_c = pre_r*2, pre_c*2
        drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in drc:
            cur_r, cur_c = pre_r+dr, pre_c+dc
            if not (0 <= cur_r < r_end and 0 <= cur_c < c_end):
                continue
            gird_c_end = len(grid[grid_r+dr])
            if grid_c+dc >= gird_c_end:
                continue
            if grid[grid_r+dr][grid_c+dc] == '1':
                continue
            yield (cur_r, cur_c)

    que = deque()
    que.append(st_node)
    dist[0][0] = 1
    while que:
        pre = que.popleft()
        pre_r, pre_c = pre
        d = dist[pre_r][pre_c]
        d += 1
        for cur in neighbors(pre):
            cur_r, cur_c = cur
            if dist[cur_r][cur_c] <= d:
                continue
            dist[cur_r][cur_c] = d
            que.append(cur)
    ans = dist[-1][-1]
    if ans == float('inf'):
        ans = 0
    print(ans)


main()
