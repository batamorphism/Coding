# N個の整数A[0],..,A[n-1]に対して
# 0<=i<j<Nを満たす全てのi,jについて、abs(A[i]-A[j])の総和を求めよ
# N=2*10**5なので間に合わないっぽい
#
# Aをソートしておけば、絶対値を外すことが可能
# 加減算のみとなるので、可換
# 従って、プラス部分の総和とマイナス部分の総和をとって、最後に引けばよい
# 各A[i]に対し、プラス部分として出てくる回数はi回、
# マイナス部分として出てくる回数はn-1-i回である

def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    plus = 0
    minus = 0
    for i in range(n):
        plus += i*A[i]
        minus += (n-1-i)*A[i]
    print(plus-minus)


main()
