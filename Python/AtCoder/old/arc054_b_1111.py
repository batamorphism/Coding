# 黄金分割探索
# 黄金比 = 1:(1+5**0.5)/2
gold_ratio = (1 + 5**0.5) / 2


def main():
    p = float(input())

    def fnc(x):
        speed = 2**(-x/1.5)
        return x + p*speed

    # 黄金探索
    le = 0
    ri = p
    err = 1e-10
    # le0とri0を黄金比で分割したleとriを求める
    delta = (ri-le)/(1+gold_ratio)
    le += delta
    ri -= delta

    le_val = fnc(le)
    ri_val = fnc(ri)
    delta = ri-le
    while delta > err:
        delta /= gold_ratio
        if le_val > ri_val:
            le, le_val = ri, ri_val
            ri = ri + delta
            ri_val = fnc(ri)
        else:
            ri, ri_val = le, le_val
            le = le - delta
            le_val = fnc(le)

    print(le_val)


main()
