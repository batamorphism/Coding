# 右に同じ数字が続く場合は、操作Bの逆
# 違う数字が出たタイミングで、操作Aの逆
from collections import deque


def main():
    n = int(input())
    A = deque(list(map(int, input().split())))
    flag = 0

    while A:
        # B チェック
        while A:
            if A and (A[-1] ^ flag) == 0:
                A.pop()
            else:
                break
        if not A:
            break
        # Aをやる
        if (A[0] ^ flag) == 1:
            print('No')
            return
        A.popleft()
        # flip(A) これはTLE
        flag ^= 1

    print('Yes')


main()
