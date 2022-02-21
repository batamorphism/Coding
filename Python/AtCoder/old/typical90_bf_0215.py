from functools import lru_cache


def main():
    n, k = map(int, input().split())

    def one_step(x):
        y_list = map(int, str(x))
        y = sum(y_list)
        z = (x+y) % 100000
        return z

    @lru_cache(maxsize=None)
    def many_step(x, k):
        # one_step(x)をk回繰り返す
        # kが大きい値の時はあまり呼ばれず、kが小さい値ほど頻繁に呼ばれる
        # したがって、鳩の巣原理的に、メモが十分に機能する
        if k == 0:
            return x
        if k % 2 == 1:
            x = one_step(x)
        x = many_step(x, k//2)
        x = many_step(x, k//2)
        return x

    x = n
    x = many_step(x, k)
    print(x)


main()
