# 01-BFS
# 0~3で向きを管理する
# 前回と同じ距離ならば距離+0、そうでないならば距離+1
from collections import deque
INF = 10**9


def main():
    # input
    r_end, c_end = map(int, input().split())
    st_r, st_c = map(int, input().split())
    en_r, en_c = map(int, input().split())
    st_r -= 1
    st_c -= 1
    en_r -= 1
    en_c -= 1
    grid = [input() for _ in range(r_end)]

    drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 01BFS
    D = [[[INF]*4 for _ in range(c_end)] for _ in range(r_end)]
    que = deque()
    que.append((st_r, st_c, -1, -1))
    for ori in range(4):
        D[st_r][st_c][ori] = -1

    while que:
        pre_r, pre_c, pre_ori = que.popleft()
        if (pre_r, pre_c) == (en_r, en_c):
            break
        for cur_ori in range(4):
            dr, dc = drc[cur_ori]
            cur_r = pre_r + dr
            cur_c = pre_c + dc
            if not(0 <= cur_r < r_end and 0 <= cur_c < c_end):
                continue
            if grid[cur_r][cur_c] == '#':
                continue
            if cur_ori == pre_ori:
                # 距離0 ただし同じ進行方向のみ
                pre_d = D[pre_r][pre_c][pre_ori]
                cur_d = pre_d
                if D[cur_r][cur_c][cur_ori] <= cur_d:
                    continue
                D[cur_r][cur_c][cur_ori] = cur_d
                que.appendleft((cur_r, cur_c, cur_ori))
            else:
                # 距離1
                pre_d = min(D[pre_r][pre_c])
                # print(pre_d)
                cur_d = pre_d + 1
                if D[cur_r][cur_c][cur_ori] <= cur_d:
                    continue
                D[cur_r][cur_c][cur_ori] = cur_d
                que.append((cur_r, cur_c, cur_ori))

    ans = min(D[en_r][en_c])
    print(ans)


main()
