from itertools import permutations
INF = 10**9


def main():
    n = int(input())
    # A[人][区間] に係る時間
    A = [list(map(int, input().split())) for _ in range(n)]

    m = int(input())
    incorrect = [set() for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        incorrect[x].add(y)
        incorrect[y].add(x)

    ans = INF
    for perm in permutations(range(n)):
        time = 0
        for aft_i in range(n):
            aft = perm[aft_i]
            # 最初の一人目は特段指定なし
            if aft_i == 0:
                time = A[aft][aft_i]
                continue
            bef = perm[aft_i-1]
            if bef in incorrect[aft]:
                # print(bef, aft, perm, incorrect)
                time = INF
                break
            time += A[aft][aft_i]
        # print(time, perm)
        ans = min(ans, time)

    if ans == INF:
        ans = -1
    print(ans)


main()
