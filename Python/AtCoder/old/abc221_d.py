def main():
    # imos
    n = int(input())
    imos0 = {}
    for _ in range(n):
        a, b = map(int, input().split())
        imos0[a] = imos0.get(a, 0)+1
        imos0[a+b] = imos0.get(a+b, 0)-1
    imos = sorted(imos0.items())

    ans = [0]*(n+1)
    cnt = 0
    pre_day = 0
    for day, delta in imos:
        ans[cnt] += day-pre_day
        cnt += delta
        pre_day = day

    print(*ans[1:])


main()
