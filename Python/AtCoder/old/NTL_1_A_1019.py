def main():
    n = int(input())
    n_ = n
    m = int(n**0.5)+10
    ans = []
    for i in range(2, m):
        if n % i == 0:
            while n % i == 0:
                ans.append(i)
                n //= i
        if n == 1:
            break
    if n != 1:
        ans.append(n)
    print(str(n_)+':', *ans)


main()
