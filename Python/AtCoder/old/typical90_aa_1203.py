def main():
    n = int(input())
    S_list = [input() for _ in range(n)]
    user_list = set()

    for day, name in enumerate(S_list, 1):
        if name not in user_list:
            print(day)
            user_list.add(name)


main()
