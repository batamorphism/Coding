from itertools import combinations


def main():
    n, m = map(int, input().split())
    relation_set = set()
    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        if x > y:
            x, y = y, x
        relation_set.add((x, y))

    for i in range(n):
        relation_set.add((i, i))

    ans = -1
    S_end = 1 << n
    for S in range(S_end):
        group = []
        for i in range(n):
            if S & (1 << i):
                group.append(i)
        is_ok = True
        for x, y in combinations(group, 2):
            if (x, y) not in relation_set:
                is_ok = False
                break
        if is_ok:
            ans = max(ans, len(group))

    print(ans)


main()
