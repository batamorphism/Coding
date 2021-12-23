def main():
    m = int(input())
    search_set = set()
    for _ in range(m):
        x, y = map(int, input().split())
        search_set.add((x, y))

    n = int(input())
    all_set = set()
    for _ in range(n):
        x, y = map(int, input().split())
        all_set.add((x, y))

    # basis_point = search_set[0] <- BAD
    basis_point = list(search_set)[0]  # <- GOOD

    for point in all_set:
        dx, dy = point[0] - basis_point[0], point[1] - basis_point[1]
        search_offset_set = set()
        for x, y in search_set:
            search_offset_set.add((x + dx, y + dy))
        if search_offset_set.issubset(all_set):
            print(dx, dy)
            return


main()
