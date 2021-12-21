def main():
    r_end, c_end, k, max_cost = map(int, map(int, input().split()))
    # 累積和は1-index
    r_end += 1
    c_end += 1
    town = [[0]*(c_end+1)]
    for _ in range(r_end-1):
        foo = list(map(int, map(int, input().split())))
        foo = [0] + foo
        town.append(foo)
    del foo
    # sum_of[r][c]: <=r, <=c
    sum_of = [[0]*c_end for _ in range(r_end)]
    for r in range(r_end):
        for c in range(c_end):
            if r == 0 or c == 0:
                sum_of[r][c] = 0
                continue
            sum_of[r][c] = (
                town[r][c]
                + sum_of[r][c-1]
                + sum_of[r-1][c]
                - sum_of[r-1][c-1]
            )

    def calc_measure(r0, c0, r1, c1):
        return (r1-r0)*(c1-c0)

    def calc_cost(r0, c0, r1, c1):
        co1 = sum_of[r1][c1]-sum_of[r1][c0]-sum_of[r0][c1]+sum_of[r0][c0]
        co2 = calc_measure(r0, c0, r1, c1)*k
        return co1+co2

    ans = 0
    for r0 in range(r_end):
        for c0 in range(c_end):
            for r1 in range(r0, r_end):
                for c1 in range(c0, c_end):
                    cost = calc_cost(r0, c0, r1, c1)
                    if cost <= max_cost:
                        ans = max(calc_measure(r0, c0, r1, c1), ans)
    print(ans)


main()
