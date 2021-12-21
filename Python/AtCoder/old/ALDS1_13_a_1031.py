import copy
INF = 10**9


def main():
    k = int(input())
    Queen_list = [['.']*8 for _ in range(8)]
    for _ in range(k):
        r, c = map(int, input().split())
        Queen_list[r][c] = 'Q'

    def check(node, r, c):
        for dr in range(-8, 9):
            r1 = r+dr
            if r1 < 0 or r1 >= 8:
                continue
            if node[r1][c] == 'Q':
                return False
        for dc in range(-8, 9):
            c1 = c+dc
            if c1 < 0 or c1 >= 8:
                continue
            if node[r][c1] == 'Q':
                return False
        for d in range(-8, 9):
            r1, c1 = r+d, c+d
            if c1 < 0 or c1 >= 8 or r1 < 0 or r1 >= 8:
                continue
            if node[r1][c1] == 'Q':
                return False
        for d in range(-8, 9):
            r1, c1 = r+d, c-d
            if c1 < 0 or c1 >= 8 or r1 < 0 or r1 >= 8:
                continue
            if node[r1][c1] == 'Q':
                return False
        return True

    def nei_of(node):
        for r in range(8):
            for c in range(8):
                if check(node, r, c):
                    ret = copy.deepcopy(node)
                    ret[r][c] = 'Q'
                    yield ret

    def tuple2d(arr):
        arr = tuple(map(tuple, arr))
        return arr

    dist = {}

    def dfs(pre):
        d = dist[tuple2d(pre)]
        if d == 8:
            for r in pre:
                print(''.join(r))
            exit()
        d += 1
        for cur in nei_of(pre):
            if dist.get(tuple2d(cur), INF) <= d:
                continue
            dist[tuple2d(cur)] = d
            dfs(cur)
            # print(cur)

    st = Queen_list
    tuple2d(st)
    dist[tuple2d(st)] = k
    dfs(st)


main()
