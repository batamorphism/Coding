def main():
    n = int(input())
    ans = 0
    # x, y独立に考える
    # 1次元ならば、xがAの中央値であるときに最小となる
    A = []
    B = []
    for _ in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    A.sort()
    B.sort()
    x = A[n//2]
    y = B[n//2]

    for a, b in zip(A, B):
        ans += dist(a, b, x, y)

    print(ans)


def dist(a1, b1, a2, b2):
    return abs(a1 - a2) + abs(b1 - b2)


main()
