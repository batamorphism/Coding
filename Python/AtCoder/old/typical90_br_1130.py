# xy独立に考える
# x, yのそれぞれ中央値に発電所を立てればよい
def main():
    n = int(input())
    mid = n // 2
    X = []
    Y = []
    for _ in range(n):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    X.sort()
    Y.sort()
    x_mid = X[mid]
    y_mid = Y[mid]

    ans = 0
    for x in X:
        ans += abs(x - x_mid)
    for y in Y:
        ans += abs(y - y_mid)
    print(ans)


main()
