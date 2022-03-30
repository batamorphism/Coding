# 01BFS
from collections import deque


def main():
    INF = float('inf')
    r_end, c_end = map(int, input().split())
    grid = [input() for _ in range(r_end)]

    dist = [[INF]*c_end for _ in range(r_end)]
    dist[0][0] = 0
    que = deque([(0, 0)])

    def cost0_nei_of(pre_r, pre_c):
        drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dr, dc in drc:
            cur_r = pre_r + dr
            cur_c = pre_c + dc
            if not (0 <= cur_r < r_end and 0 <= cur_c < c_end):
                continue
            if grid[cur_r][cur_c] == '#':
                continue
            yield cur_r, cur_c

    def cost1_nei_of(pre_r, pre_c):
        # #...#
        # .....
        # ..@..
        # .....
        # #...#
        dr_list = dc_list = [-2, -1, 0, 1, 2]
        for dr in dr_list:
            for dc in dc_list:
                if abs(dr) == abs(dc) == 2:
                    continue
                if dr == dc == 0:
                    continue
                cur_r, cur_c = pre_r + dr, pre_c + dc
                if not (0 <= cur_r < r_end and 0 <= cur_c < c_end):
                    continue
                yield cur_r, cur_c

    while que:
        pre_r, pre_c = que.popleft()
        pre_d = dist[pre_r][pre_c]
        # 0-cost
        # キューの左に追加
        for cur_r, cur_c in cost0_nei_of(pre_r, pre_c):
            cur_d = pre_d
            if dist[cur_r][cur_c] <= cur_d:
                continue
            dist[cur_r][cur_c] = cur_d
            que.appendleft((cur_r, cur_c))

        # 1-cost
        # キューの右に追加
        for cur_r, cur_c in cost1_nei_of(pre_r, pre_c):
            cur_d = pre_d + 1
            if dist[cur_r][cur_c] <= cur_d:
                continue
            dist[cur_r][cur_c] = cur_d
            que.append((cur_r, cur_c))

    ans = dist[-1][-1]
    print(ans)


main()
