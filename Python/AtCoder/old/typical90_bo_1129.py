from collections import deque
# print(int('100', 3))


def main():
    n, k = map(int, input().split())
    for _ in range(k):
        n = func(n)
    print(n)


def func(n):
    # nをstrに変換
    n = str(n)
    # nを8進法で読む
    n = int(n, 8)
    # nを9進法で表現
    n = bin_9(n)
    # nに出てくる8を5に
    n = n.replace('8', '5')
    # nをintに
    n = int(n)
    return n


def bin_9(n):
    # nを9進法で表現
    que = deque()
    while n > 0:
        que.appendleft(n % 9)
        n //= 9
    ret = ''.join(map(str, que))
    if ret == '':
        ret = '0'
    return ret


main()
