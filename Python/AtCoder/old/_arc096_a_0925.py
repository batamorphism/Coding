def main():
    a, b, c, x, y = map(int, input().split())
    INF = 1001001001
    ans = INF
    for ab_pizza in range(max(x, y)*2+1):
        a_pizza = max(x-ab_pizza//2, 0)
        b_pizza = max(y-ab_pizza//2, 0)
        cost = a_pizza*a+b_pizza*b+ab_pizza*c
        ans = min(cost, ans)
    print(ans)


main()
