# BFSたくさん
from collections import deque

def main():
    INF = float('inf')
    r_end, c_end, n = map(int, input().split())
    grid = [input() for _ in range(r_end)]

    path_list = [[None, None] for _ in range(n)]
    for r in range(r_end):
        for c in range(c_end):
            if grid[r][c] == '.':
                continue
            if grid[r][c] == 'X':
                continue
            if grid[r][c] == 'S':
                path_list[0][0] = (r, c)
                continue
            cnt = int(grid[r][c])
            path_list[cnt-1][1] = (r, c)
            if cnt < n:
                path_list[cnt][0] = (r, c)

    def nei_of(pre_r, pre_c):
        drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dr, dc in drc:
            cur_r = pre_r + dr
            cur_c = pre_c + dc
            if cur_r < 0 or cur_r >= r_end:
                continue
            if cur_c < 0 or cur_c >= c_end:
                continue
            if grid[cur_r][cur_c] == 'X':
                continue
            yield cur_r, cur_c

    # print(path_list)
    # path_listの順に、最短経路を求めていく
    ans = 0
    for path in path_list:
        fr, to = path
        fr_r, fr_c = fr
        to_r, to_c = to
        dist = [[INF]*c_end for _ in range(r_end)]
        dist[fr_r][fr_c] = 0
        que = deque()
        que.append((fr_r, fr_c))
        while que:
            pre_r, pre_c = que.popleft()
            pre_d = dist[pre_r][pre_c]
            cur_d = pre_d + 1
            for cur_r, cur_c in nei_of(pre_r, pre_c):
                if dist[cur_r][cur_c] <= cur_d:
                    continue
                dist[cur_r][cur_c] = cur_d
                que.append((cur_r, cur_c))
        ans += dist[to_r][to_c]

    print(ans)


main()
