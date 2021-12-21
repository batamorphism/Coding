def main():
    n = int(input())
    nn = n
    m = int(n**0.5+10)
    ans = []
    for d in range(2, m):
        while n % d == 0:
            ans.append(d)
            n //= d

    if n != 1:
        ans.append(n)

    print(f'{nn}:', *ans)


main()
