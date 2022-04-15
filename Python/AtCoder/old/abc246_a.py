from collections import Counter


def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    # 1個しかないやつ
    x_list = [x1, x2, x3]
    y_list = [y1, y2, y3]
    cntx_of = Counter(x_list)
    cnty_of = Counter(y_list)
    ans_x = 0
    ans_y = 0
    for key, value in cntx_of.items():
        if value == 1:
            ans_x = key
    for key, value in cnty_of.items():
        if value == 1:
            ans_y = key

    print(ans_x, ans_y)


main()
