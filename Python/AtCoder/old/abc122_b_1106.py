ACGT = set('ACGT')


def main():
    S = list(input())
    ans = 0
    for delta in range(len(S)+1):
        for le in range(len(S)):
            ri = le + delta
            if ri > len(S):
                break
            sub_S = S[le:ri]
            if check(sub_S):
                ans = max(ans, len(sub_S))
    print(ans)


def check(sub_S):
    for i in range(len(sub_S)):
        if sub_S[i] not in ACGT:
            return False
    return True


main()
