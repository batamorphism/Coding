# 幅優先探索で最短距離を計算
# h*w-sum(grid)-最短距離が答え
# ただし、スタート地点の距離は1とする
from collections import deque
INF = float('inf')


def main():
    r_end, c_end = map(int, input().split())
    grid = [list(input()) for _ in range(r_end)]
    D = [[INF] * c_end for _ in range(r_end)]

    def nei_of(pre_r, pre_c):
        drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dr, dc in drc:
            cur_r, cur_c = pre_r+dr, pre_c+dc
            if not (0 <= cur_r < r_end and 0 <= cur_c < c_end):
                continue
            if grid[cur_r][cur_c] == '#':
                continue
            yield cur_r, cur_c

    st_node = (0, 0)
    D[0][0] = 1
    que = deque([st_node])
    while que:
        pre_r, pre_c = que.popleft()
        pre_d = D[pre_r][pre_c]
        d = pre_d+1
        for cur_r, cur_c in nei_of(pre_r, pre_c):
            if D[cur_r][cur_c] > d:
                D[cur_r][cur_c] = d
                que.append((cur_r, cur_c))

    if D[r_end-1][c_end-1] == INF:
        print(-1)
        return

    ans = r_end*c_end
    for r in range(r_end):
        for c in range(c_end):
            if grid[r][c] == '#':
                ans -= 1
    ans -= D[r_end-1][c_end-1]
    print(ans)


main()
