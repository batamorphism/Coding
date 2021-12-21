import sys
sys.setrecursionlimit(10**6)


# Union_Find
# 赤マスを追加した時、上下左右の赤マスとUnionする
def main():
    r_end, c_end = map(int, input().split())

    # Setup Union Find
    # (r, c) -> (r * c_end + c)
    i_end = r_end*c_end
    par = [i for i in range(i_end)]

    def find(x):
        if par[x] == x:
            return x
        else:
            par[x] = find(par[x])
            return par[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        par[x] = y
        return

    def same(x, y):
        return find(x) == find(y)

    grid = [[0]*c_end for _ in range(r_end)]

    q = int(input())
    for _ in range(q):
        r, *query = map(int, input().split())
        if r == 1:
            r, c = query
            r -= 1
            c -= 1
            i = r*c_end + c
            grid[r][c] = 1
            drc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in drc:
                rr = r + dr
                cc = c + dc
                ii = rr*c_end + cc
                if 0 <= rr < r_end and 0 <= cc < c_end:
                    if grid[rr][cc] == 1:
                        union(i, ii)
        else:
            r1, c1, r2, c2 = query
            r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1
            i1 = r1*c_end + c1
            i2 = r2*c_end + c2
            if same(i1, i2) and grid[r1][c1] == 1 and grid[r2][c2] == 1:
                print("Yes")
            else:
                print("No")


main()
