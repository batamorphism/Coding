import itertools
INF = 10**9


def main():
    # N <= 10なので、N!ってそんなに大きくない
    n = int(input())
    A = [list(map(int, input().split())) for _ in range(n)]

    m = int(input())
    ng_list = [set() for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        ng_list[x].add(y)
        ng_list[y].add(x)

    perms = itertools.permutations(range(n))

    ans = INF
    for perm in perms:
        #  区間d, 区間d-1を走った人, 区間dを走る人 からなるループ
        perm = list(perm)
        time = 0
        bef_i_list = [-1] + perm[:-1]
        cur_i_list = perm
        for d, bef_i_cur_i in enumerate(zip(bef_i_list, cur_i_list)):
            bef_i, cur_i = bef_i_cur_i
            if cur_i in ng_list[bef_i]:
                time = INF
                break
            d_time = A[cur_i][d]
            time += d_time
        ans = min(ans, time)

    if ans == INF:
        ans = -1
    print(ans)


main()
