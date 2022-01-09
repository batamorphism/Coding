from itertools import product


# setで考える
def main():
    n = int(input())
    S_set = set()
    T_set = set()
    S = [input() for _ in range(n)]
    T = [input() for _ in range(n)]

    for r, c in product(range(n), repeat=2):
        if S[r][c] == '#':
            S_set.add((r, c))
        if T[r][c] == '#':
            T_set.add((r, c))

    if len(S_set) != len(T_set):
        print('No')
        return

    for _ in range(4):
        if check(S_set, T_set):
            print('Yes')
            return
        S_set = rotate(S_set)
        # display(S_set, n)

    print('No')


def check(S_set: set, T_set: set) -> bool:
    # S_setとT_setが平行移動させて同じかどうか
    # これは、Sの要素を平行移動させたものがTに含まれているかどうかで判定する
    base_point = list(S_set)[0]
    for t_point in T_set:
        diff_r = t_point[0] - base_point[0]
        diff_c = t_point[1] - base_point[1]
        is_subset = True
        for s_point in S_set:
            offset_point = (s_point[0] + diff_r, s_point[1] + diff_c)
            if offset_point not in T_set:
                is_subset = False
                break
        if is_subset:
            return True
    return False


def rotate(S_set):
    # S_setの各要素を90度回転させる
    # r -> c, c -> -r
    new_S_set = set()
    for r, c in S_set:
        new_S_set.add((c, -r))
    return new_S_set


def display(S_set: set, n):
    grid = [['.']*n for _ in range(n)]
    for r, c in S_set:
        grid[r][c] = '#'
    for row in grid:
        print(''.join(row))


main()
