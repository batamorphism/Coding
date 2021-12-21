def main():
    p = float(input())

    def func(x):
        # x年待機した後計算する場合に係る時間
        speed = 2**(-x/1.5)
        return p*speed+x

    # funcの最小値を求める
    # funcは下に凸である
    ok = 0
    ng = p
    err = 10**(-8)
    while ng-ok > err:
        mid_l = ok+(ng-ok)/3
        mid_r = ok+(ng-ok)/3*2
        if func(mid_l) > func(mid_r):
            ok = mid_l
        else:
            ng = mid_r

    print(func(ok))


main()
