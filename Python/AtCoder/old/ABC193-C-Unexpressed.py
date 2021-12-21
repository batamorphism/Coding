# 整数Nに対し、1～Nの整数のうち2以上の整数a, bを用いてa**bと表せないものはいくつあるか
# (あるいは、表せるものはいくつあるか)
# N<=10**10なので全探索はむり
# n = a**b <-> logn = bloga
# b = log(n)/log(a)
# b = log_a(n)
# a = n**1/b
# aとして考えられる範囲は、2以上、n**1/b以下
# bとして考えられる範囲は、2以上、log_a(n)以下

import math


def main():
    n = int(input())
    ans = set()
    for b in range(2, round(math.log(n, 2))+1):
        for a in range(2, round(n**(1/b)+1)):
            if a**b <= n:
                ans.add(a**b)

    print(n - len(ans))


main()