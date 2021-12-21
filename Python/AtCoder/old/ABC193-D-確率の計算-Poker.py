# カードは、1,..,9がそれぞれk枚ずつの9k枚ある
# 高橋くんと青木君にそれぞれ、4枚を表向きに、1枚を裏向きに配る
# (確定したカードは8枚、未確定のカードは9k-8枚)
# この状態で、高橋君があるカードsを引く確率は、9k-8枚のうちsの残り枚数


def main():
    k = int(input())
    s = input()
    t = input()
    s_open = list(map(int, list(s[:4])))
    t_open = list(map(int, list(t[:4])))
    # 9*9の81通りについて、勝つか負けるか決定する

    total = 0
    for s_close in range(1, 10):
        for t_close in range(1, 10):
            s_all = s_open + [s_close]
            t_all = t_open + [t_close]
            if calc_score(s_all) > calc_score(t_all):  # 高橋くんの勝利
                # s_closeがk枚のうち後何枚残っているか
                remain_s_close = k - (s_open+t_open).count(s_close)
                # t_closeがk枚のうち後何枚残っているか
                remain_t_close = k - (s_all+t_open).count(t_close)
                total += remain_s_close * remain_t_close

    # 全体の組み合わせは、(9k-8)*(9k-9)
    print(total/((9*k-8)*(9*k-9)))


def calc_score(cards: list):
    ret = 0
    for i in range(1, 10):
        ret += i*(10**cards.count(i))
    return ret


main()
