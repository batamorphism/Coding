mod = 10**9 + 7


def main():
    k = int(input())
    # DP[val] = DP[val - 1] + DP[val - 2] + ... + DP[val - 9]
    if k % 9 != 0:
        print(0)
        return

    DP = [0] * (k+1)
    for val in range(k+1):
        if val == 0:
            DP[val] = 1
            continue
        dp = 0
        for num in range(1, 10):
            if val - num >= 0:
                dp += DP[val - num]
        DP[val] = dp % mod

    print(DP[k])


main()
