def main():
    n, k, a = map(int, input().split())
    num = (k+a-1) % n
    if num == 0:
        num = n
    print(num)


main()
