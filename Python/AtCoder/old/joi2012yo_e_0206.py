from collections import deque


def main():
    r_end, c_end = map(int, input().split())
    pre_grid = []
    pre_grid.append([0] + [0]*r_end + [0])
    for _ in range(c_end):
        col = [0] + list(map(int, input().split())) + [0]
        pre_grid.append(col)
    pre_grid.append([0] + [0]*r_end + [0])
    # 転置してやる
    grid = list(map(list, zip(*pre_grid)))

    r_end += 2
    c_end += 2

    def nei_of(pre_r, pre_c):
        if pre_r + 1 < r_end:
            yield pre_r + 1, pre_c
        if pre_c + 1 < c_end:
            yield pre_r, pre_c + 1
        if pre_r - 1 >= 0:
            yield pre_r - 1, pre_c
        if pre_c - 1 >= 0:
            yield pre_r, pre_c - 1
        if pre_c % 2 == 0:
            # rを-1, cを+-1する
            cur_r = pre_r - 1
            if cur_r >= 0:
                if pre_c + 1 < c_end:
                    yield cur_r, pre_c + 1
                if pre_c - 1 >= 0:
                    yield cur_r, pre_c - 1
        else:
            # rを+1, cを+-1
            cur_r = pre_r + 1
            if cur_r < r_end:
                if pre_c + 1 < c_end:
                    yield cur_r, pre_c + 1
                if pre_c - 1 >= 0:
                    yield cur_r, pre_c - 1

    # BFS
    que = deque()
    ans = 0
    col = [['w']*c_end for _ in range(r_end)]
    que.append((0, 0))
    while que:
        pre_r, pre_c = que.popleft()
        for cur_r, cur_c in nei_of(pre_r, pre_c):
            if col[cur_r][cur_c] == 'b':
                continue
            if grid[cur_r][cur_c]:
                # 建物であった場合は、到達フラグは立てず、答えは+1
                ans += 1
                continue
            else:
                col[cur_r][cur_c] = 'b'
                que.append((cur_r, cur_c))

    print(ans)


main()
