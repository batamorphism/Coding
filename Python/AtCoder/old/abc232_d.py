# 遠回りは存在しない
# DFSして距離の最大値
from collections import deque


def main():
    r_end, c_end = map(int, input().split())
    grid = [list(input()) for _ in range(r_end)]

    INF = float('inf')
    dist = [[INF] * c_end for _ in range(r_end)]

    que = deque()
    que.append((0, 0))
    dist[0][0] = 1

    def nei_of(pre):
        pre_r, pre_c = pre
        drc = [(1, 0), (0, 1)]
        for dr, dc in drc:
            cur_r, cur_c = pre_r + dr, pre_c + dc
            if not (0 <= cur_r < r_end and 0 <= cur_c < c_end):
                continue
            if grid[cur_r][cur_c] == '#':
                continue
            yield cur_r, cur_c

    while que:
        pre = que.popleft()
        pre_r, pre_c = pre
        pre_d = dist[pre_r][pre_c]
        cur_d = pre_d + 1
        for cur_r, cur_c in nei_of(pre):
            if dist[cur_r][cur_c] > cur_d:
                dist[cur_r][cur_c] = cur_d
                que.append((cur_r, cur_c))

    ans = 0
    for r in range(r_end):
        for c in range(c_end):
            if dist[r][c] == INF:
                continue
            ans = max(ans, dist[r][c])

    print(ans)


main()
