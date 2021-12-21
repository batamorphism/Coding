def main():
    n_end, m = map(int, input().split())
    nei_of = [set() for _ in range(n_end)]
    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        nei_of[x].add(y)
        nei_of[y].add(x)

    ALL_n = 1 << n_end

    ans = 0
    for bit in range(ALL_n):
        n_list = []
        for n in range(n_end):
            if bit & (1 << n):
                n_list.append(n)
        is_ok = True
        for n1 in n_list:
            for n2 in n_list:
                if n1 == n2:
                    continue
                if n2 not in nei_of[n1]:
                    is_ok = False
                    break
        if is_ok:
            ans = max(ans, len(n_list))

    print(ans)


main()
