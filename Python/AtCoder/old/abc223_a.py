def main():
    x = int(input())
    if x == 0:
        ans = 'No'
    elif x % 100 == 0:
        ans = 'Yes'
    else:
        ans = 'No'
    print(ans)


main()
