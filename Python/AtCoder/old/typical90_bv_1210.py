def main():
    n = int(input())
    S = input()
    pot = 0
    for i, s in enumerate(S):
        if s == 'b':
            pot += 2**i
        elif s == 'c':
            pot += 2**i * 2
    print(pot)


main()
