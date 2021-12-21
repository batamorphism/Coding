from collections import deque
INF = 10**9


def main():
    r_end, c_end, n = map(int, input().split())
    town = [input() for _ in range(r_end)]

    fr_node_list = [(0, 0)]*n
    to_node_list = [(0, 0)]*n
    for r in range(r_end):
        for c in range(c_end):
            if town[r][c] == 'S':
                fr_node_list[0] = (r, c)
            for i in range(1, n+1):
                if town[r][c] == str(i):
                    to_node_list[i-1] = (r, c)
                    if i < n:
                        fr_node_list[i] = (r, c)

    ans = 0
    dr_list = [0, 1, 0, -1]
    dc_list = [1, 0, -1, 0]
    # BFSをn回実施する
    # 各回のBFSは、n-1からnまでの最短距離を探す
    for fr_node, to_node in zip(fr_node_list, to_node_list):
        que = deque()
        dist = [[INF]*c_end for _ in range(r_end)]
        fr_r, fr_c = fr_node
        dist[fr_r][fr_c] = 0
        que.append(fr_node)
        while que:
            pre_node = que.popleft()
            pre_r, pre_c = pre_node
            if pre_node == to_node:
                ans += dist[pre_r][pre_c]
                break  # goto next bfs
            d = dist[pre_r][pre_c]
            d += 1
            for dr, dc in zip(dr_list, dc_list):
                cur_r, cur_c = pre_r+dr, pre_c+dc
                if cur_r < 0 or cur_r >= r_end or cur_c < 0 or cur_c >= c_end:
                    continue
                if dist[cur_r][cur_c] <= d:
                    continue
                if town[cur_r][cur_c] == 'X':
                    continue
                dist[cur_r][cur_c] = d
                que.append((cur_r, cur_c))

    print(ans)


main()
