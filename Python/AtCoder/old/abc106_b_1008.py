def check(n: int):
    i_end = int(n**0.5+10)
    ans = set()
    for i in range(1, i_end):
        if n % i == 0:
            ans.add(i)
            ans.add(n//i)
    return len(ans)


def main():
    n_max = int(input())
    ans = 0
    for n in range(1, n_max+1, 2):
        cnt = check(n)
        if cnt == 8:
            ans += 1
    print(ans)


main()
