from collections import deque
# しゃくとり法
# 円環は2倍


def main():
    n = int(input())
    A = list(map(int, input().split()))
    tmp = sum(A)
    if tmp % 10 != 0:
        print('No')
        return
    target = tmp // 10
    A += A

    que = deque()
    a_sum = 0
    for a in A:
        que.append(a)
        a_sum += a
        while que and not (a_sum <= target):
            rm = que.popleft()
            a_sum -= rm
        # print(que, a_sum, target)
        if a_sum == target:
            print('Yes')
            return
    print('No')


main()
