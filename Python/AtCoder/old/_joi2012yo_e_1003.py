from collections import deque


def main():
    """
    BFSをして、壁にぶつかった回数を数え上げればよい
    (r, c)のnei_ofは...画像はc, rの順なので注意
    r % 2 == 1の場合、八個の近傍のうち、(r-1, c+1), (r-1, C-1)の2つを除く
    r % 2 == 0の場合、八個の近傍のうち、(r+1, c+1), (r+1, C-1)の2つを除く
    """
    INF = 10**10
    w, h = map(int, input().split())
    # 上下左右に[0]を付け足す
    r_end = h+2
    c_end = w+2
    table = []
    for r in range(r_end):
        if r == 0 or r == r_end-1:
            table.append([0]*c_end)
            continue
        tmp = list(map(int, input().split()))
        tmp = [0] + tmp + [0]
        table.append(tmp)

    # DFB
    ans = 0
    que = deque()
    dist = [[INF]*c_end for _ in range(r_end)]
    start_node = (0, 0)
    dist[0][0] = 0
    que.append(start_node)
    while que:
        pre_node = que.popleft()
        pre_r, pre_c = pre_node
        nei = nei_of(pre_node, r_end, c_end)
        for cur_node in nei:
            cur_r, cur_c = cur_node
            d = dist[pre_r][pre_c]+1
            if dist[cur_r][cur_c] <= d:
                continue
            if table[cur_r][cur_c] == 1:
                # 壁にぶつかった
                ans += 1
                continue
            dist[cur_r][cur_c] = d
            que.append(cur_node)
    print(ans)


def nei_of(node: tuple, r_end: int, c_end: int):
    # 壁は無視して近傍を6つ返す
    # r % 2 == 1の場合、八個の近傍のうち、(r+1, c-1), (r-1, c-1)の2つを除く
    # r % 2 == 0の場合、八個の近傍のうち、(r+1, c+1), (r-1, c+1)の2つを除く
    pre_r, pre_c = node
    dr_list = [-1, 0, 1]
    dc_list = [-1, 0, 1]
    ans = []
    for dr in dr_list:
        for dc in dc_list:
            cur_r = pre_r + dr
            cur_c = pre_c + dc
            if cur_r < 0 or cur_r >= r_end or cur_c < 0 or cur_c >= c_end:
                continue
            if dr == dc == 0:
                continue
            if pre_r % 2 == 0:
                if dr == 1 and dc == 1:
                    continue
                if dr == -1 and dc == 1:
                    continue
            else:
                if dr == 1 and dc == -1:
                    continue
                if dr == -1 and dc == -1:
                    continue
            ans.append((cur_r, cur_c))
    return ans


main()
