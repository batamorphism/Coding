def main():
    x0 = float(input())
    x = int(x0)
    y = int((x0 - x)*10)
    ans = str(x)
    if y <= 2:
        ans += '-'
    elif y <= 6:
        ans += ''
    else:
        ans += '+'
    print(ans)


main()