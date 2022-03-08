from collections import defaultdict
from collections import deque


# 01bfs
# 状態付き
# 座標圧縮
def main():
    r_end, c_end, n = map(int, input().split())
    st_r, st_c = map(lambda x: int(x)-1, input().split())
    en_r, en_c = map(lambda x: int(x)-1, input().split())
    r_list = []
    c_list = []
    for _ in range(n):
        x, y = map(int, input().split())
        r_list.append(x)
        c_list.append(y)
    # 座標圧縮
    zipper_r = {r: i for i, r in enumerate(sorted(set(r_list + [st_r, en_r])))}
    zipper_c = {c: i for i, c in enumerate(sorted(set(c_list + [st_c, en_c])))}
    r_list = [zipper_r[r] for r in r_list]
    c_list = [zipper_c[c] for c in c_list]
    r_end = max(r_list)+1
    c_end = max(c_list)+1
    grid = [[0]*c_end for _ in range(r_end)]
    for r, c in zip(r_list, c_list):
        grid[r][c] = 1
    st_r = zipper_r[st_r]
    en_r = zipper_r[en_r]
    st_c = zipper_c[st_c]
    en_c = zipper_c[en_c]

    def nei_of_0(pre_r, pre_c, pre_ori):
        drc_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        drc = drc_list[pre_ori]
        nex_r, nex_c = pre_r + drc[0], pre_c + drc[1]
        if not (0 <= nex_r < r_end and 0 <= nex_c < c_end):
            return
        if grid[nex_r][nex_c] == 1:
            return
        yield nex_r, nex_c, pre_ori

    def nei_of_1(pre_r, pre_c):
        drc_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        drc = drc_list[pre_ori]
        for ori in range(4):
            drc = drc_list[ori]
            nex_r, nex_c = pre_r + drc[0], pre_c + drc[1]
            if not (0 <= nex_r < r_end and 0 <= nex_c < c_end):
                continue
            if grid[nex_r][nex_c] == 1:
                continue
            yield nex_r, nex_c, nex_ori

    # (r, c, ori)における移動回数
    INF = float('inf')
    dist_of = [[[INF]*4 for _ in range(c_end)] for _ in range(r_end)]
    que = deque()
    for ori in range(4):
        que.append((st_r, st_c, ori))
        dist_of[st_r][st_c][ori] = 0
    # 01bfs
    while que:
        pre_r, pre_c, pre_ori = que.popleft()
        pre_d = dist_of[pre_r][pre_c][pre_ori]
        # 距離0
        cur_d = pre_d
        for nex_r, nex_c, nex_ori in nei_of_0(pre_r, pre_c, pre_ori):
            if dist_of[nex_r][nex_c][nex_ori] <= cur_d:
                continue
            dist_of[nex_r][nex_c][nex_ori] = cur_d
            que.appendleft((nex_r, nex_c, nex_ori))
        # 距離1
        cur_d = pre_d + 1
        for nex_r, nex_c, nex_ori in nei_of_1(pre_r, pre_c):
            if dist_of[nex_r][nex_c][nex_ori] <= cur_d:
                continue
            dist_of[nex_r][nex_c][nex_ori] = cur_d
            que.append((nex_r, nex_c, nex_ori))

    ans = INF
    for ori in range(ori):
        ans = min(ans, dist_of[en_r][en_c][ori])
    print(ans)


main()
