# x軸とy軸独立に考える
# 移動できる候補のリストをもって置き、全操作終了後にen_x, en_yにいるかをDP
def main():
    s = input() + 'T'
    en_x, en_y = map(int, input().split())
    x_list = []
    y_list = []

    is_x = True
    is_first = True
    cnt = 0
    for c in s:
        if c == 'F':  # 今向いている向きに移動
            cnt += 1
        else:  # 左右に90度回転
            if is_x:
                if is_first:
                    x_list.append((cnt,))
                else:
                    x_list.append((cnt, -cnt))
            else:
                y_list.append((cnt, -cnt))
            is_x = not is_x
            is_first = False
            cnt = 0

    if check(x_list, en_x) and check(y_list, en_y):
        print('Yes')
    else:
        print('No')


def check(x_list, en_x):
    # x_listの値を足したり引いたりして、en_xになるかを判定
    dp = set([0])
    for dx_list in x_list:
        nex_dp = set()
        for dx in dx_list:
            for cur_x in dp:
                nex_x = cur_x + dx
                nex_dp.add(nex_x)
        dp = nex_dp.copy()
    return en_x in dp


main()
