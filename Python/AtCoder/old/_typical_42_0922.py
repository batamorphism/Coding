def main():
    k = int(input())
    p = 10**9+7
    # DP[i]=各桁の和がiになる組み合わせ
    DP = [0]*(k+1)
    DP[0] = 1
    for i in range(1, k+1):
        s = 0
        for j in range(1, 10):
            if i-j < 0:
                break
            s += DP[i-j]
        DP[i] = s % p

    if k % 9 == 0:
        print(DP[k])
    else:
        print(0)


main()
