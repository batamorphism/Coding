def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))

    # 櫛
    is_prime = [True]*(10**5+1)
    div = [1]*(10**5+1)
    is_prime[0] = False
    is_prime[1] = False
    for num in range(2, 10**5+1):
        if is_prime[num]:
            div[num] = num
            for num2 in range(num**2, 10**5+1, num):
                is_prime[num2] = False
                div[num2] = num

    # 全てのaと互いに素な数kをすべて列挙する
    # Aの素因数全てを列挙し、
    # kの素因数が1つでも含まれていたらアウト
    prime_factor_of_A = set()
    for a in A:
        while a != 1:
            prime_factor_of_A.add(div[a])
            a //= div[a]

    # print(prime_factor_of_A)

    def generate_prime_factor(n):
        while n != 1:
            yield div[n]
            n //= div[n]

    ans = []
    for k in range(1, m+1):
        can_add = True
        for fac in generate_prime_factor(k):
            if fac in prime_factor_of_A:
                can_add = False
                break
        if can_add:
            ans.append(k)

    print(len(ans))
    for a in ans:
        print(a)


main()
