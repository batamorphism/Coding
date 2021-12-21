# 幅優先探索
# S->1->2->...->nの順に探索する
from collections import deque


def main():
    r_end, c_end, n = map(int, input().split())
    grid = [input() for _ in range(r_end)]

    st_node_list = [(-1, -1)]*n
    en_node_list = [(-1, -1)]*n
    for r in range(r_end):
        for c in range(c_end):
            if grid[r][c] == 'S':
                st_node_list[0] = (r, c)
            for i in range(1, n+1):
                if grid[r][c] == str(i):
                    if i < n:
                        st_node_list[i] = (r, c)
                    en_node_list[i-1] = (r, c)

    def nei_of(pre):
        pre_r, pre_c = pre
        drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in drc:
            cur_r = pre_r + dr
            cur_c = pre_c + dc
            if not (0 <= cur_r < r_end and 0 <= cur_c < c_end):
                continue
            if grid[cur_r][cur_c] == 'X':
                continue
            yield (cur_r, cur_c)

    ans = 0
    for st_node, en_node in zip(st_node_list, en_node_list):
        que = deque()
        D = [[float('inf')]*c_end for _ in range(r_end)]
        que.append(st_node)
        st_r, st_c = st_node
        D[st_r][st_c] = 0
        while que:
            pre = que.popleft()
            if pre == en_node:
                break
            pre_r, pre_c = pre
            pre_d = D[pre_r][pre_c]
            d = pre_d + 1
            for cur in nei_of(pre):
                cur_r, cur_c = cur
                if D[cur_r][cur_c] <= d:
                    continue
                D[cur_r][cur_c] = d
                que.append(cur)
        en_r, en_c = en_node
        ans += D[en_r][en_c]

    print(ans)


main()
