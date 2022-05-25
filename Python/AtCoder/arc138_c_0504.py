# 理論値が答え
def main():
    n = int(input())
    A = list(map(int, input().split()))
    # Aのうち、小さいほうn個ならばFalseとする
    B = [(a_i, i) for i, a_i in enumerate(A)]
    B.sort()
    is_use = [-1]*n
    for a_i, i in B[:n//2]:
        is_use[i] = 1
    ans = sum([b for b, i in B[n//2:]])

    # 累積和が最小となるところが答え
    for i in range(1, n):
        is_use[i] += is_use[i-1]

    pos_val = min(is_use)
    pos = is_use.index(pos_val)
    print(pos)
    print(ans)


main()
