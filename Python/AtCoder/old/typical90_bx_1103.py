from collections import deque


def main():
    n = int(input())
    A = list(map(int, input().split()))
    total = sum(A)
    if total % 10 != 0:
        print('No')
        return

    search = total // 10
    # ピースの長さがsearchとなるような区間を探す
    # 尺取り法
    # 円環で考えたいので、Aは2倍にする
    A += A
    que = deque()
    size = 0
    for a in A:
        que.append(a)
        size += a
        while que and not (size <= search):
            size -= que.popleft()
        if size == search:
            print('Yes')
            return

    print('No')


main()
