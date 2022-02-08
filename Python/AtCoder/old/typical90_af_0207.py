# 全探索
from itertools import permutations


def main():
    node_end = int(input())
    INF = float('inf')
    # A[区間][選手] = その選手がその区間を走るのにかかる時間
    A = [list(map(int, input().split())) for _ in range(node_end)]
    m = int(input())
    # 選手iと相性の悪い選手の集合
    ng_bef_set_list = [set() for _ in range(node_end)]
    for _ in range(m):
        x, y = map(lambda x: int(x)-1, input().split())
        ng_bef_set_list[x].add(y)
        ng_bef_set_list[y].add(x)

    ans = INF
    for perm in permutations(range(node_end)):
        # perm順で走った場合の時間
        cur_ans = 0
        bef = -1
        for section, human in enumerate(perm):
            # cost = A[section][human]
            cost = A[human][section]
            if bef in ng_bef_set_list[human]:
                cur_ans = INF
                break
            cur_ans += cost
            bef = human
        ans = min(ans, cur_ans)

    if ans == INF:
        ans = -1
    print(ans)


main()

