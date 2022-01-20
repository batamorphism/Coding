# a人組を作ると、人数はaの倍数のうち超えないものの最大値となる
# すなわち
# x -> x - x % a
# 操作後がx人とする
# a人組を作った後の人数がxとは
# x % a != 0 -> 存在しえない
# それ以外
# 操作前の人数は、x～x+a-1の間
def main():
    k = int(input())
    A = list(map(int, input().split()))
    lo = 2
    hi = 2
    for a in reversed(A):
        # loを超える最小のaの倍数を求める
        # lo/aを切り上げして、aをかける
        nex_lo = (-(-lo//a))*a
        nex_hi = (hi//a)*a + a - 1
        if nex_hi < nex_lo:
            print(-1)
            return
        lo = nex_lo
        hi = nex_hi
    print(lo, hi)


main()
