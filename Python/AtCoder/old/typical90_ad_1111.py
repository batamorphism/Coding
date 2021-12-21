# エラトステネスの篩


def main():
    n, k = map(int, input().split())
    is_prime = [True] * (n+1)
    cnt_of = [0] * (n+1)

    num_end = n+1
    for num in range(num_end):
        if num <= 1:
            is_prime[num] = False
            cnt_of[num] = 0
            continue

        if is_prime[num]:
            cnt_of[num] = 1
            for num2 in range(num*2, num_end, num):
                is_prime[num2] = False
                cnt_of[num2] += 1

    ans = sum([1 for num in cnt_of if num >= k])
    print(ans)


main()
