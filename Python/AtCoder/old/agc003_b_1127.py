def main():
    n = int(input())
    A = []
    ans = 0
    for i in range(n):
        a = int(input())
        if a == 0:
            ans += solve(A)
            A = []
        else:
            A.append(a)
    ans += solve(A)

    print(ans)


def solve(A):
    val = sum(A)
    val //= 2
    # print(A, val)
    return val


main()
