def main():
    s = input()
    s = s[::-1]
    s = s.replace('9', '-')
    s = s.replace('6', '9')
    s = s.replace('-', '6')
    print(s)


main()