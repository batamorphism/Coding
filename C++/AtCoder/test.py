def main():
    n = int(input())
    S = []
    for _ in range(n):
        s = input()
        S.append(s)
    S.reverse()
    print(*S, sep='\n')


main()
