def main():
    n = int(input())
    A_set = set()
    for _ in range(n):
        A = tuple(map(int, input().split()))
        A_set.add(A)

    print(len(A_set))


main()
