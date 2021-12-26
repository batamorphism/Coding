def main():
    n = int(input())
    bef_n = n

    m = int(n**0.5) + 10
    prime_factor_list = []
    for factor in range(2, m):
        while n % factor == 0:
            prime_factor_list.append(factor)
            n //= factor

    if n != 1:
        prime_factor_list.append(n)

    print(str(bef_n) + ':', *prime_factor_list)


main()
