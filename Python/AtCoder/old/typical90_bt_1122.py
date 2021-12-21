# 深さ優先探索で、バックトラックして、全部調べる
def main():
    r_end, c_end = map(int, input().split())
    grid = [input() for _ in range(r_end)]

    color = [['w']*c_end for _ in range(r_end)]
    st_pos = (0, 0)

    def nei_of(pre):
        pre_r, pre_c = pre
        drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dr, dc in drc:
            cur_r, cur_c = pre_r + dr, pre_c + dc
            if not(0 <= cur_r < r_end and 0 <= cur_c < c_end):
                continue
            if grid[cur_r][cur_c] == '#':
                continue
            yield (cur_r, cur_c)

    def dfs(pre, dist, ans):
        if pre == st_pos and dist != 0:
            return max(ans, dist)
        for cur in nei_of(pre):
            r, c = cur
            if color[r][c] == 'w':
                color[r][c] = 'g'
                dist += 1
                ans = max(ans, dfs(cur, dist, ans))
                dist -= 1
                color[r][c] = 'w'
        return ans

    dist = 0
    ans = 0
    for r in range(r_end):
        for c in range(c_end):
            st_pos = (r, c)
            ans = max(ans, dfs(st_pos, dist, 0))

    if ans <= 2:
        ans = -1
    print(ans)


main()
