from collections import Counter


def main():
    a = list(input())
    n = len(a)
    cnt_of = Counter(a)

    nC2 = n*(n-1)//2
    ans = nC2
    for cnt in cnt_of.values():
        cntC2 = cnt*(cnt-1)//2
        ans -= cntC2
    print(ans+1)


main()
