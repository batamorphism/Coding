from collections import Counter


def main():
    n = int(input())
    A = list(map(int, input().split()))
    cnt_of = Counter(A)
    print(len(cnt_of))


main()
