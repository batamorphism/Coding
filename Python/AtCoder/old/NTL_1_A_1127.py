def main():
    n = int(input())
    nn = n
    m = int(n**0.5+10)
    ans_list = []

    for factor in range(2, m+1):
        while n % factor == 0:
            ans_list.append(factor)
            n //= factor

    if n != 1:
        ans_list.append(n)

    ans_list.sort()

    print(str(nn)+":", *ans_list)


main()
