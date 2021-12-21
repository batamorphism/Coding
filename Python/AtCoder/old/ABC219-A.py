def main():
    x = int(input())
    ans = -1
    if x<40 :
        ans = 40-x
    elif x<70:
        ans = 70-x
    elif x<90:
        ans = 90-x

    if ans == -1:
        print('expert')
    else:
        print(ans)


main()
