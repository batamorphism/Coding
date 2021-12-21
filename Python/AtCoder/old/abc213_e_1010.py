from collections import deque


def main():
    r_end, c_end = map(int, input().split())
    town = [list(input()) for _ in range(r_end)]

    # 01BFS
    INF = 10**9
    dist = [[INF]*c_end for _ in range(r_end)]
    que = deque()
    st_node = (0, 0)
    dist[0][0] = 0
    que.append(st_node)
    while que:
        pre_node = que.popleft()
        pre_r, pre_c = pre_node

        # cost 0 is dfs
        nei_of = get_nei_of_c0(pre_node)
        d = dist[pre_r][pre_c]
        for cur_node in nei_of:
            cur_r, cur_c = cur_node
            if cur_r < 0 or cur_r >= r_end or cur_c < 0 or cur_c >= c_end:
                continue
            if town[cur_r][cur_c] == '#':
                continue
            if dist[cur_r][cur_c] <= d:
                continue
            dist[cur_r][cur_c] = d
            que.appendleft(cur_node)

        # cost 1 is bfs
        nei_of = get_nei_of_c1(pre_node)
        d = dist[pre_r][pre_c]
        d += 1
        for cur_node in nei_of:
            cur_r, cur_c = cur_node
            if cur_r < 0 or cur_r >= r_end or cur_c < 0 or cur_c >= c_end:
                continue
            if dist[cur_r][cur_c] <= d:
                continue
            dist[cur_r][cur_c] = d
            que.append(cur_node)

    print(dist[-1][-1])


def get_nei_of_c0(pre_node):
    # 上下左右
    pre_r, pre_c = pre_node
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    ret = []
    for i in range(4):
        cur_r = pre_r + dr[i]
        cur_c = pre_c + dc[i]
        ret.append((cur_r, cur_c))
    return ret


def get_nei_of_c1(pre_node):
    # #...#
    # .....
    # ..@..
    # .....
    # #...#
    pre_r, pre_c = pre_node
    dr_list = list(range(-2, 3))
    dc_list = list(range(-2, 3))
    ret = []
    for dr in dr_list:
        for dc in dc_list:
            if abs(dr) == 2 and abs(dc) == 2:
                continue
            if (dr, dc) == (0, 0):
                continue
            cur_r = pre_r + dr
            cur_c = pre_c + dc
            ret.append((cur_r, cur_c))
    return ret


main()
