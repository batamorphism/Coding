def main():
    sign_cnt = int(input())
    sign_list = [list(map(int, input().split())) for _ in range(sign_cnt)]
    star_cnt = int(input())
    star_set = set(tuple(map(int, input().split())) for _ in range(star_cnt))
    x0, y0 = sign_list[0]
    for star in star_set:
        x1, y1 = star
        offset_x = x1-x0
        offset_y = y1-y0
        # sign_listをoffsetしたものが、star_setに含まれるか
        is_contain = True
        for sign in sign_list:
            x, y = sign
            x += offset_x
            y += offset_y
            if (x, y) not in star_set:
                is_contain = False
                break
        if is_contain:
            print(offset_x, offset_y)
            return


main()
