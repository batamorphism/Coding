from collections import deque


def main():
    h, w = map(int, input().split())
    S = []
    for _ in range(h):
        S.append(list(*input().split()))

    dist = [[10**10]*w for _ in range(h)]

    que = deque()
    que.appendleft((0, 0))
    dist[0][0] = 0
    dx = [+0, +1, -0, -1]
    dy = [+1, +0, -1, -0]
    dx1_list = [+2, +1, +0, -1, -2]
    dy1_list = [+2, +1, +0, -1, -2]

    # start 01 BFS
    while que:
        x, y = que.popleft()
        # calc neighbor of x, y cost 0
        for i in range(4):
            curr_x = x+dx[i]
            curr_y = y+dy[i]
            is_inside = 0 <= curr_x < w and 0 <= curr_y < h
            if not is_inside:
                continue
            if dist[curr_y][curr_x] <= dist[y][x]:
                continue
            if S[curr_y][curr_x] == '#':
                continue

            # can move cost 0
            dist[curr_y][curr_x] = dist[y][x]
            que.appendleft((curr_x, curr_y))  # コスト0なので左に足す

        # calc neighbor of x, y cost 1

        for dx1 in dx1_list:
            for dy1 in dy1_list:
                if abs(dx1) == 2 and abs(dy1) == 2:  # 範囲外
                    continue
                if dx1 == 0 and dy1 == 0:  # 移動していない
                    continue
                curr_x = x+dx1
                curr_y = y+dy1
                is_inside = 0 <= curr_x < w and 0 <= curr_y < h
                if not is_inside:
                    continue
                if dist[curr_y][curr_x] <= dist[y][x]+1:
                    continue

                # can move cost 1
                dist[curr_y][curr_x] = dist[y][x] + 1
                que.append((curr_x, curr_y))

    print(dist[-1][-1])


main()
