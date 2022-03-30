def main():
    n = int(input())
    user_set = set()
    ans_list = []
    for day in range(1, n+1):
        s = input()
        if s not in user_set:
            user_set.add(s)
            ans_list.append(day)
    print(*ans_list, sep='\n')


main()
