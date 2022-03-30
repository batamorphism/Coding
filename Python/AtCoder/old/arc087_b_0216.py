def main():
    s = input()
    x, y = map(int, input().split())
    # 縦と横を独立に考える
    # Tで囲まれたFの個数を数える
    x_len = []
    y_len = []
    cur_len = 0
    is_x = 1
    is_first = True
    for c in s:
        if c == 'T':
            if is_first:
                st_x, st_y = cur_len, 0
                is_first = False
            else:
                if is_x:
                    x_len.append(cur_len)
                else:
                    y_len.append(cur_len)
            is_x = 1 ^ is_x
            cur_len = 0
            continue
        cur_len += 1

    if is_first:
        st_x, st_y = cur_len, 0
        is_first = False
    else:
        if is_x:
            x_len.append(cur_len)
        else:
            y_len.append(cur_len)

    # x_lenを足したり引いたりして、xにできるか
    if check(x_len, x-st_x) and check(y_len, y-st_y):
        print('Yes')
    else:
        print('No')


def check(arr, val):
    # arrの要素を足したり引いたりして、valにできるか
    # dp = i番目まで見て、実現可能な要素の集合
    dp = set([0])
    for a in arr:
        new_dp = set()
        for cur_val in dp:
            new_val = cur_val + a
            new_dp.add(new_val)
            new_val = cur_val - a
            new_dp.add(new_val)
        dp = new_dp.copy()
    if val in dp:
        return True
    else:
        return False


main()
