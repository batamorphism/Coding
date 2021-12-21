# 整数からなる公差1の等差数列
# 1,2,3とか
# -2,-1,0,-1,2とか
# 始点a,終点bの総和は、(a+b)/2*(a-b+1)
# a+b = c, a-b+1 = dと置くと
# c*d/2
# したがって、2*nを2つの積に分けた場合の個数を求める

def main():
    n = int(input())
    ans = 0
    for i in range(1, int((2*n)**0.5)+1):
        if 2*n % i == 0:
            c = (2*n)//i
            d = i
            a = (c+(d-1))/2
            b = c-a
            if float.is_integer(a) and float.is_integer(b):
                if c == d:
                    ans += 1
                else:
                    ans += 2
            
    print(ans)


main()