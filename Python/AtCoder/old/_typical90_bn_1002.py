def main():
    n = int(input())
    # E[i][j]を、X[i]>X[j]となる確率とする
    # E[i][j]の総和が解となる
    hi = []
    lo = []
    for _ in range(n):
        a, b = map(int, input().split())
        hi.append(b)
        lo.append(a)
    E = [[0]*n for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            total = (hi[i]-lo[i]+1)*(hi[j]-lo[j]+1)
            cnt = 0
            for val_i in range(lo[i], hi[i]+1):
                for val_j in range(lo[j], hi[j]+1):
                    if val_i > val_j:
                        cnt += 1
            E[i][j] = cnt/total
            ans += cnt/total
    print(ans)


main()
