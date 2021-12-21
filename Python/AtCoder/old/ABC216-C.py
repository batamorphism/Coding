def main():
    n = int(input())
    curr_n = n
    ans = ''
    while curr_n != 0:
        if curr_n%2 == 0:
            ans = 'B'+ans
            curr_n = curr_n//2
        else:
            ans = 'A'+ans
            curr_n = curr_n -1

    print(ans)


main()