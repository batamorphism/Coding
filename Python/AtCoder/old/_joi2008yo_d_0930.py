def main():
    m = int(input())
    search_list = []
    for _ in range(m):
        x, y = map(int, input().split())
        search_list.append((x, y))
    n = int(input())
    star_list = []
    for _ in range(n):
        x, y = map(int, input().split())
        star_list.append((x, y))

    base_star = search_list[0]
    base_x, base_y = base_star
    for star in star_list:
        x, y = star
        offset_x, offset_y = x-base_x, y-base_y
        is_find = True
        for search in search_list:
            s_x, s_y = search
            s_x += offset_x
            s_y += offset_y
            if (s_x, s_y) not in star_list:
                is_find = False
                break
        if is_find:
            print(offset_x, offset_y)
            break


main()
