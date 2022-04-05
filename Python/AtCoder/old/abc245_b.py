def main():
    n = int(input())
    A = list(map(int, input().split()))
    A_set = set(A)
    for i in range(n+1):
        if i not in A_set:
            print(i)
            return


main()
