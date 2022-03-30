import sys
sys.setrecursionlimit(10**6)


def main():
    r_end, c_end = map(int, input().split())
    q = int(input())
    i_end = rc2i(r_end-1, c_end-1, r_end, c_end)+1
    col = [0] * i_end  # 赤色で塗られたら1
    # union find
    par = [i for i in range(i_end)]
    siz = [1]*i_end

    def find(x):
        if x == par[x]:
            return x
        par[x] = find(par[x])
        return par[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if siz[x] > siz[y]:
            x, y = y, x
        par[x] = y
        siz[y] += siz[x]
        siz[x] = 0

    def is_same(x, y):
        return find(x) == find(y)

    def nei_of(r, c):
        drc_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dr, dc in drc_list:
            cur_r = r + dr
            cur_c = c + dc
            # 範囲内かつ、赤色である
            if not (0 <= cur_r < r_end and 0 <= cur_c < c_end):
                continue
            i = rc2i(cur_r, cur_c, r_end, c_end)
            if not col[i]:
                continue
            yield cur_r, cur_c

    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    for query in query_list:
        q_type = query[0]
        if q_type == 1:
            r, c = query[1], query[2]
            r -= 1
            c -= 1
            i = rc2i(r, c, r_end, c_end)
            col[i] = 1
            for cur_r, cur_c in nei_of(r, c):
                cur_i = rc2i(cur_r, cur_c, r_end, c_end)
                union(i, cur_i)
        else:
            fr_r, fr_c, to_r, to_c = query[1], query[2], query[3], query[4]
            fr_r -= 1
            fr_c -= 1
            to_r -= 1
            to_c -= 1
            fr_i = rc2i(fr_r, fr_c, r_end, c_end)
            to_i = rc2i(to_r, to_c, r_end, c_end)
            if is_same(fr_i, to_i) and col[fr_i] and col[to_i]:
                print('Yes')
            else:
                print('No')


def rc2i(r, c, r_end, c_end):
    return r * c_end + c


main()
