import sys
sys.setrecursionlimit(10**6)


def main():
    r_end, c_end = map(int, input().split())
    q = int(input())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]

    def rc2index(r, c):
        return r*c_end + c

    grid = [['w']*c_end for _ in range(r_end)]

    def nei_of(r, c):
        # r, cの上下左右のうち、赤いものを返す
        drc_list = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for dr, dc in drc_list:
            cur_r, cur_c = r+dr, c+dc
            if not(0 <= cur_r < r_end and 0 <= cur_c < c_end):
                continue
            if not grid[cur_r][cur_c] == 'r':
                continue
            yield cur_r, cur_c

    # setup Union Find
    node_end = r_end*c_end
    par = [i for i in range(node_end)]

    def find(x):
        if x == par[x]:
            return x
        par[x] = find(par[x])
        return par[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        par[x] = y

    def same(x, y):
        return find(x) == find(y)

    for query in query_list:
        if query[0] == 1:
            # union query
            _, r, c = query
            r -= 1
            c -= 1
            pre_node = rc2index(r, c)
            grid[r][c] = 'r'
            for cur_r, cur_c in nei_of(r, c):
                cur_node = rc2index(cur_r, cur_c)
                # print('1---', pre_node, cur_node)
                union(pre_node, cur_node)
        else:
            _, r0, c0, r1, c1 = query
            r0 -= 1
            c0 -= 1
            r1 -= 1
            c1 -= 1
            node0, node1 = rc2index(r0, c0), rc2index(r1, c1)
            # print('2---', node0, node1)
            if grid[r0][c0] != 'r' or grid[r1][c1] != 'r':
                print('No')
            elif same(node0, node1):
                print('Yes')
            else:
                print('No')


main()
