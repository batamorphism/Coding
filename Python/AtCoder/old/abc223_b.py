def main():
    S = input()
    n = len(S)
    max_ans = S
    min_ans = S
    for _ in range(n):
        S = shift(S)
        if max_ans < S:
            max_ans = S
        if min_ans > S:
            min_ans = S
    print(min_ans)
    print(max_ans)


def shift(S):
    return S[1:]+S[0]


main()
