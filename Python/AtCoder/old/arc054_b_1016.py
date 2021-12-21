def main():
    p = float(input())
    # t+p*2**(-t/1.5) の最小値
    # 下に凸の時は三分探索

    def f(t):
        return t+p*2**(-t/1.5)

    # df(t)=0となるtを求める。絶対誤差10**-8以下
    err = 10**(-8)
    le = 0
    ri = 10**18+1
    while ri-le > err:
        tri_le = le+(ri-le)/3
        tri_ri = le+(ri-le)/3*2
        if f(tri_ri) > f(tri_le):
            ri = tri_ri
        else:
            le = tri_le
    print(f(le))


main()
