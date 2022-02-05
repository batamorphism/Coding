import time
from functools import lru_cache


def main():
    node_end, rule_end = map(int, input().split())
    # rule_of[今まで使った要素数] = (y_i以下の数はz_i個しか存在しない)
    rule_of = [[] for _ in range(node_end+1)]
    for _ in range(rule_end):
        x, y, z = map(int, input().split())
        # y だけは0-indexed
        y -= 1
        rule_of[x].append((y, z))

    st_time = time.perf_counter()

    ALL = 1 << node_end
    DP = [0]*ALL
    DP[0] = 1

    for cur_S in range(ALL):
        for nex_node in range(node_end):
            if cur_S >> nex_node & 1:
                continue
            nex_S = cur_S | 1 << nex_node
            size = popcount(nex_S)
            rule = rule_of[size]
            # nex_S に、y以下の要素はz個以下しか存在しない
            is_ok = True
            for y, z in rule:
                lower_y = nex_S & ((1 << (y+1)) - 1)
                if popcount(lower_y) > z:
                    is_ok = False
                    break
            if not is_ok:
                continue
            DP[nex_S] += DP[cur_S]

    ans = DP[ALL-1]
    print(ans)
    en_time = time.perf_counter()
    # print(en_time-st_time)


@lru_cache(maxsize=None)
def popcount(S):
    return bin(S).count('1')


main()
