from collections import deque


def main():
    n, k = map(int, input().split())
    S = [int(input()) for _ in range(n)]
    # コーナーケース
    if 0 in S:
        print(n)
        return

    que = deque()
    prod = 1
    ans = 0
    for s in S:
        que.append(s)
        prod *= s
        while que and not prod <= k:
            rm = que.popleft()
            prod //= rm
        ans = max(ans, len(que))

    print(ans)


main()
