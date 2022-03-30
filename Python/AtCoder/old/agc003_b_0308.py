def main():
    n = int(input())
    value_list = []
    A = [int(input()) for _ in range(n)] + [0]
    value = 0
    for a in A:
        if a != 0:
            value += a
        else:
            value_list.append(value)
            value = 0

    ans = 0
    for value in value_list:
        ans += value // 2
    print(ans)


main()
