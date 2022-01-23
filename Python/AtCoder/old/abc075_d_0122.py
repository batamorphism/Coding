from itertools import product


# x_hi, x_lo, y_hi, y_loの候補が少ないことを使い、全探索
def main():
    INF = float('inf')
    n, k = map(int, input().split())
    X = []
    Y = []
    for _ in range(n):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

    ans = INF
    # for i0, i1, i2, i3 in product(range(n), repeat=4):
    for i0 in range(n):
        for i1 in range(i0, n):
            for i2 in range(n):
                for i3 in range(i2, n):
                    x_hi = X[i0]
                    x_lo = X[i1]
                    y_hi = Y[i2]
                    y_lo = Y[i3]
                    if x_hi < x_lo:
                        x_hi, x_lo = x_lo, x_hi
                    if y_hi < y_lo:
                        y_hi, y_lo = y_lo, y_hi
                    cur_ans = (x_hi - x_lo)*(y_hi - y_lo)
                    if cur_ans >= ans:
                        continue

                    # この領域に囲まれている点の数を数える
                    # 高速化余地あり
                    cnt = 0
                    for x, y in zip(X, Y):
                        if x_lo <= x <= x_hi and y_lo <= y <= y_hi:
                            cnt += 1
                    if cnt >= k:
                        ans = min(ans, (x_hi - x_lo)*(y_hi - y_lo))

    print(ans)


main()
