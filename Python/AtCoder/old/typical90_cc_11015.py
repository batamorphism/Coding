def main():
    n, k = map(int, input().split())
    # matrix[a][b] = 身長a, 体重bの人数
    MAX_VAL = 5001
    matrix = [[0]*MAX_VAL for _ in range(MAX_VAL)]
    for _ in range(n):
        a, b = map(int, input().split())
        matrix[a][b] += 1
    # matrixの累積和
    cumsum = [[0]*MAX_VAL for _ in range(MAX_VAL)]
    for a in range(1, MAX_VAL):
        for b in range(1, MAX_VAL):
            cumsum[a][b] = matrix[a][b]+cumsum[a-1][b]+cumsum[a][b-1]-cumsum[a-1][b-1]

    ans = 0
    for a0 in range(MAX_VAL):
        a1 = a0+k+1
        if a1 >= MAX_VAL:
            continue
        for b0 in range(MAX_VAL):
            b1 = b0+k+1
            if b1 >= MAX_VAL:
                continue
            num = cumsum[a1][b1]-cumsum[a1][b0]-cumsum[a0][b1]+cumsum[a0][b0]
            ans = max(num, ans)

    print(ans)


main()
