from collections import deque
INF = 10**9


def solve(ans_list):
    c_end, r_end = map(int, input().split())
    if c_end == 0 and r_end == 0:
        return False
    table = []
    for _ in range(2*r_end-1):
        table.append(input())

    def can_move(r, c, dr, dc, table):
        # r, cのdr, dcの向きに壁がないことを確認する
        # table上では、r, cは2倍される
        rr = r*2
        cc = c*2
        rr_end = r_end*2-1
        cc_end = c_end*2-1
        rr += dr
        cc += dc
        if not (0 <= rr < rr_end and 0 <= cc < cc_end):
            return False
        # print(table[rr][cc])
        if table[rr][cc] == '1':
            return False
        return True

    def nei_of(pre):
        r, c = pre
        DR = [0, 0, -1, 1]
        DC = [1, -1, 0, 0]
        for dr, dc in zip(DR, DC):
            if can_move(r, c, dr, dc, table):
                yield (r+dr, c+dc)

    # BFS
    que = deque()
    dist = [[INF]*c_end for _ in range(r_end)]
    dist[0][0] = 1
    que.append((0, 0))
    while que:
        pre = que.popleft()
        r, c = pre
        d = dist[r][c]
        d += 1
        for cur in nei_of(pre):
            r, c = cur
            if dist[r][c] > d:
                dist[r][c] = d
                que.append(cur)

    ans = dist[-1][-1]
    if ans == INF:
        ans = 0
    ans_list.append(ans)
    return True


def main():
    ans_list = []
    while 1:
        is_continue = solve(ans_list)
        if not is_continue:
            break
    for ans in ans_list:
        print(ans)


main()
# solve()