# PINは1000通りしかない
import itertools


def main():
    _ = int(input())
    S = input()
    A = []
    for s in S:
        A.append(int(s))

    def check(A, pin):
        ind = 0
        for a in A:
            if pin[ind] == a:
                ind += 1
                if ind >= 3:
                    return True
        return False

    ans = 0
    prod = itertools.product(range(10), repeat=3)
    for pin in prod:
        if check(A, pin):
            ans += 1

    print(ans)

main()
