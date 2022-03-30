from collections import deque


def main():
    r_end, c_end = map(int, input().split())
    grid = [input() for _ in range(r_end)]
    INF = float('inf')

    def nei_of(pre_r, pre_c):
        drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dr, dc in drc:
            cur_r, cur_c = pre_r + dc, pre_c + dr
            if not (0 <= cur_r < r_end and 0 <= cur_c < c_end):
                continue
            if not (grid[cur_r][cur_c] == '.'):
                continue
            yield cur_r, cur_c

    # 幅優先探索
    dist = [[INF]*c_end for _ in range(r_end)]
    dist[0][0] = 0
    que = deque([(0, 0)])
    while que:
        pre_r, pre_c = que.popleft()
        cur_d = dist[pre_r][pre_c]+1
        for cur_r, cur_c in nei_of(pre_r, pre_c):
            if dist[cur_r][cur_c] <= cur_d:
                continue
            dist[cur_r][cur_c] = cur_d
            que.append((cur_r, cur_c))
    tot = 0
    for row in grid:
        tot += row.count('.')
    ans = tot - dist[r_end-1][c_end-1] - 1
    if ans == -INF:
        ans = -1
    print(ans)


main()
