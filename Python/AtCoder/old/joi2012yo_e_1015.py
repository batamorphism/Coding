from collections import deque


def main():
    # 偶数行だと左にずれて
    # 奇数行だと右にずれる
    end_c, end_r = map(int, input().split())
    end_c += 2
    end_r += 2
    town = []
    for i in range(end_r):
        if i == 0 or i == end_r-1:
            blank_row = [0]*end_c
            town.append(blank_row)
            continue
        r = list(map(int, input().split()))
        r = [0] + r + [0]
        town.append(r)

    def nei_of(pre_node):
        pre_r, pre_c = pre_node
        dr_list = dc_list = list(range(-1, 2))
        for dr in dr_list:
            for dc in dc_list:
                if dr == 0 and dc == 0:
                    continue
                if pre_r % 2 == 1:
                    # 偶数行は左にずれているので、左上と左下は読まない
                    if dc == -1 and abs(dr) == 1:
                        continue
                else:
                    if dc == 1 and abs(dr) == 1:
                        continue
                cur_r, cur_c = pre_r+dr, pre_c+dc
                if cur_r < 0 or cur_r >= end_r or cur_c < 0 or cur_c >= end_c:
                    continue
                yield (cur_r, cur_c)

    # bfs
    ans = 0
    st_node = (0, 0)
    color = [['w']*end_c for _ in range(end_r)]
    que = deque()
    que.append(st_node)
    color[0][0] = 'g'
    while que:
        pre_node = que.popleft()
        pre_r, pre_c = pre_node
        for cur_node in nei_of(pre_node):
            cur_r, cur_c = cur_node
            if color[cur_r][cur_c] != 'w':
                continue
            if town[cur_r][cur_c] == 1:
                ans += 1
                continue
            color[cur_r][cur_c] = 'g'  # 最後に色を付ける
            que.append(cur_node)
        color[pre_r][pre_c] = 'b'

    print(ans)


main()
