# しゃくとり法
from collections import deque


def main():
    n, k = map(int, input().split())
    A = [int(input()) for _ in range(n)]

    if A.count(0):
        print(n)
        return

    que = deque()
    prod_a = 1
    ans = 0
    for a in A:
        que.append(a)
        prod_a *= a
        while que and not prod_a <= k:
            rm = que.popleft()
            prod_a //= rm
        ans = max(len(que), ans)

    print(ans)


main()
