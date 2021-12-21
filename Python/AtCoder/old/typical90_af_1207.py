from itertools import permutations
# 10! = 3_628_800
# 全探索行ける？


def main():
    n = int(input())
    A = tuple([tuple(map(int, input().split())) for _ in range(n)])
    m = int(input())
    INF = float('inf')
    XY_list = set()
    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        XY_list.add((x, y))
        XY_list.add((y, x))

    ans = INF
    for perm in permutations(range(n)):
        # print(perm)
        # 各区間iをperm[i]が走る
        pre_x = -1
        perm_ans = 0
        for j, x in enumerate(perm):
            if pre_x != -1:
                if (x, pre_x) in XY_list:
                    perm_ans = INF
                    break
            perm_ans += A[x][j]
            pre_x = x
        ans = min(ans, perm_ans)

    if ans == INF:
        ans = -1

    print(ans)


main()
