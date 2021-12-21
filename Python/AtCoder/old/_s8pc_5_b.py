def main():
    n, m = map(int, input().split())
    X = [0]*(n+m)
    Y = [0]*(n+m)
    R = [0]*(n)
    for i in range(n+m):
        if i < n:
            x, y, r = map(int, input().split())
            X[i] = x
            Y[i] = y
            R[i] = r
        else:
            x, y = map(int, input().split())
            X[i] = x
            Y[i] = y

    if m == 0:
        ans = min(R)
    else:
        ans = 10.0**10
        for p1 in range(n, n+m):
            x1 = X[p1]
            y1 = Y[p1]
            for p2 in range(n+m):
                if p1 == p2:
                    continue
                x2 = X[p2]
                y2 = Y[p2]
                dist = ((x1-x2)**2+(y1-y2)**2)**0.5
                if p2 < n:
                    ans = min(ans, dist-R[p2])
                else:
                    ans = min(ans, dist/2)

    print(ans)


main()
