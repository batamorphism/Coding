from collections import deque
INF = float('inf')


def main():
    ans_list = []
    while True:
        c_end, r_end = map(int, input().split())
        if r_end == c_end == 0:
            break
        grid = [input() for _ in range(r_end*2-1)]
        ans = solve(r_end, c_end, grid)
        ans_list.append(ans)
    for ans in ans_list:
        print(ans)


def solve(r_end, c_end, grid):
    que = deque([(0, 0)])
    dist = [[INF]*c_end for _ in range(r_end)]
    dist[0][0] = 1

    def nei_of(pre_r, pre_c):
        drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pre_grid_r = pre_r * 2
        pre_grid_c = pre_c * 2
        for dr, dc in drc:
            cur_r, cur_c = pre_r+dr, pre_c+dc
            if not (0 <= cur_r < r_end and 0 <= cur_c < c_end):
                continue
            cur_grid_r = pre_grid_r + dr
            cur_grid_c = pre_grid_c + dc
            if not grid[cur_grid_r][cur_grid_c] == '0':
                continue
            yield cur_r, cur_c

    while que:
        pre_r, pre_c = que.popleft()
        cur_d = dist[pre_r][pre_c] + 1
        for cur_r, cur_c in nei_of(pre_r, pre_c):
            if dist[cur_r][cur_c] <= cur_d:
                continue
            dist[cur_r][cur_c] = cur_d
            que.append((cur_r, cur_c))
    ans = dist[r_end-1][c_end-1]
    if ans == INF:
        ans = 0
    return ans


main()
