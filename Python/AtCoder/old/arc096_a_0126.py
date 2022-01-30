# a + ab//2 >= x
# b + ab//2 >= y
# となるようにa, b, abの組み合わせを求める
# abが決まれば、a, bが確定する
def main():
    a_cost, b_cost, ab_cost, x, y = map(int, input().split())

    ans = float('inf')
    ab_max = max(2*x, 2*y)
    for ab in range(ab_max+1):
        a = max(x - ab//2, 0)
        b = max(y - ab//2, 0)
        cost = a*a_cost + b*b_cost + ab*ab_cost
        ans = min(ans, cost)

    print(ans)


main()
