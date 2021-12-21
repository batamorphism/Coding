def cnt_factor(n):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
    return cnt


def main():
    n_end = int(input())
    n_end += 1
    ans = 0
    for n in range(1, n_end):
        if n % 2 == 0:
            continue
        if cnt_factor(n) == 8:
            ans += 1

    print(ans)


main()
