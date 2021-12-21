def main():
    n = int(input())
    S = [input() for _ in range(n)]
    user_list = set()
    ans = []
    for day, name in enumerate(S):
        if name in user_list:
            continue
        user_list.add(name)
        ans.append(day + 1)

    print(*ans)


main()
