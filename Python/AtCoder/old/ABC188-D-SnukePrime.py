# n個のサービスを、a[i]～b[i]日まで使用する
# 同時にk個のサービスを使用している場合、
# c[i]の和か、Cかどちらか小さいほうを支払う

def main():
    #Input
    n, prime_c = map(int, input().split())
    cost_gain_of = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        cost_gain_of.append([a, c])
        cost_gain_of.append([b+1, -c])
    cost_gain_of.sort()

    cost_per_day = 0
    pre_day = 0
    total_cost = 0
    for day, cost in cost_gain_of:
        total_cost += min(cost_per_day, prime_c) * (day - pre_day)
        cost_per_day += cost
        pre_day = day

    print(total_cost)


main()