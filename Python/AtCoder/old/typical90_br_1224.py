# 独立に考える
# x, yそれぞれ、中央値を取ればよい
import statistics


def main():
    n = int(input())
    X = []
    Y = []
    for _ in range(n):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

    x_mid = statistics.median_low(X)
    y_mid = statistics.median_low(Y)

    ans = 0
    for x, y in zip(X, Y):
        ans += abs(x - x_mid) + abs(y - y_mid)

    print(ans)


main()
