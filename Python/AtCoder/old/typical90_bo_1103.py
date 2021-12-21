from collections import deque


def main():
    n, k = input().split()
    k = int(k)
    for _ in range(k):
        # nは8進数
        num = 0
        for char in n:
            num *= 8
            num += int(char)

        # print(num)
        # nを9進数にする
        que = deque()
        while num > 0:
            que.appendleft(num % 9)
            num //= 9
            # print(num, que)
        # print(que)
        n = []
        while que:
            rm = que.popleft()
            if rm == 8:
                rm = 5
            n.append(rm)
        # print(n)
        # print(''.join(map(str, n))
        n = ''.join(map(str, n))
    if n == '':
        print(0)
    else:
        print(n)


main()
