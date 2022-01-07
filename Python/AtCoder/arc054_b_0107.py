def main():
    p = float(input())

    def t(x):
        if x < 0:
            return float('inf')
        time1 = x
        time2 = p * (2 ** (-x/1.5))
        return time1+time2

    def get_3_quantile(min_val, max_val):
        delta = max_val - min_val
        delta /= 3
        return min_val+delta, max_val-delta

    ok = 0
    ng = p
    diff = 1e-10
    # 3分探索
    while ng - ok > diff:
        lo, hi = get_3_quantile(ok, ng)
        if t(lo) > t(hi):
            ok = lo
        else:
            ng = hi

    print(t(ok))


main()
