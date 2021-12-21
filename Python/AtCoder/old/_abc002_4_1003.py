def main():
    n_end, pair_end = map(int, input().split())
    pair_of = [set() for _ in range(n_end)]
    for _ in range(pair_end):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        pair_of[x].add(y)
        pair_of[y].add(x)
    for n in range(n_end):
        pair_of[n].add(n)
    ALL = 1 << n_end
    ans = 0
    for bit in range(ALL):
        group = []
        for n in range(n_end):
            if bit >> n & 1:
                group.append(n)
        if len(group) <= ans:
            continue
        if not check_pair(group, pair_of):
            continue
        ans = max(len(group), ans)

    print(ans)


def check_pair(group, pair_of):
    for g1 in group:
        for g2 in group:
            if g1 not in pair_of[g2]:
                return False
    return True


main()
