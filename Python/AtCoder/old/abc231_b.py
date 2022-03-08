from collections import Counter


def main():
    _, day_end = map(int, input().split())
    A = list(map(int, input().split()))
    cnt_of = Counter(A)
    B = list(map(int, input().split()))

    for i, b_i in enumerate(B):
        if not cnt_of[b_i]:
            print('No')
            return
        cnt_of[b_i] -= 1

    print('Yes')


main()
