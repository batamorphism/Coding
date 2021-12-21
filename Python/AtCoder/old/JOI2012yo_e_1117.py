from collections import deque

def main():
    w, h = map(int, input().split())
    c_end = w+1
    r_end = h+1
    town = [[-1]*(c_end+1)]
    for r in range(1, r_end):
        row = list(map(int, input().split()))
        row = [-1] + row + [-1]
        town.append(row)
    town += [[-1]*(c_end+1)]
    c_end += 1
    r_end += 1

    def nei_of(pre):
        pre_r, pre_c = pre
        drc = [(0, -1), (0, 1)]
        if pre_r % 2 == 0:
            drc += [(-1, -1), (1, -1), (-1, 0), (1, 0)]
        else:
            drc += [(-1, 0), (1, 0), (-1, 1), (1, 1)]
        for dr, dc in drc:
            cur_r, cur_c = pre_r + dr, pre_c + dc
            if not (0 <= cur_r < r_end and 0 <= cur_c < c_end):
                continue
            yield (cur_r, cur_c)

    # 1-indexed
    que = deque()
    color = [['w']*c_end for _ in range(r_end)]
    que.append((0, 0))
    color[0][0] = 'b'

    ans = 0
    while que:
        pre = que.popleft()
        for cur in nei_of(pre):
            cur_r, cur_c = cur
            if town[cur_r][cur_c] == 1:
                # print(pre, cur)
                ans += 1
                continue
            if color[cur_r][cur_c] == 'w':
                color[cur_r][cur_c] = 'b'
                que.append(cur)

    print(ans)


main()
