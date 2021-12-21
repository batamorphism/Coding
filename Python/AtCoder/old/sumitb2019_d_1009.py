def main():
    n = int(input())
    S = input()
    ans = 0
    for one in range(10):
        one_str = str(one)
        for two in range(10):
            two_str = str(two)
            for thr in range(10):
                thr_str = str(thr)
                if check(S, one_str, two_str, thr_str):
                    ans += 1
    print(ans)


def check(S, one_str, two_str, thr_str):
    one = S.find(one_str)
    if one == -1:
        return False
    two = S[one+1:].find(two_str)
    if two == -1:
        return False
    thr = S[two+one+2:].find(thr_str)
    if thr == -1:
        return False
    return True


main()
