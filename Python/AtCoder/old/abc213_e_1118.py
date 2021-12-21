from collections import deque
INF = 10**9


def main():
    r_end, c_end = map(int, input().split())
    S = [list(input()) for _ in range(r_end)]

    def nei_0(pre):
        # 上下左右かつ、#でない
        pre_r, pre_c = pre
        drc = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dr, dc in drc:
            r = pre_r + dr
            c = pre_c + dc
            if not (0 <= r < r_end and 0 <= c < c_end):
                continue
            if S[r][c] == '#':
                continue
            yield (r, c)

    def nei_1(pre):
        # #...#
        # .....
        # ..@..
        # .....
        # #...#
        pre_r, pre_c = pre
        for dr in range(-2, 3):
            for dc in range(-2, 3):
                if abs(dr) == abs(dc) == 2:
                    continue
                r = pre_r + dr
                c = pre_c + dc
                if not (0 <= r < r_end and 0 <= c < c_end):
                    continue
                yield (r, c)

    # 01-bfs
    # setup
    D = [[INF]*c_end for _ in range(r_end)]
    que = deque()
    D[0][0] = 0
    que.append((0, 0))

    while que:
        pre = que.popleft()
        pre_r, pre_c = pre
        pre_d = D[pre_r][pre_c]

        # 0
        d = pre_d + 0
        for cur in nei_0(pre):
            cur_r, cur_c = cur
            if D[cur_r][cur_c] > d:
                D[cur_r][cur_c] = d
                que.appendleft(cur)

        # 1
        d = pre_d + 1
        for cur in nei_1(pre):
            cur_r, cur_c = cur
            if D[cur_r][cur_c] > d:
                D[cur_r][cur_c] = d
                que.append(cur)

    ans = D[-1][-1]
    print(ans)


main()
