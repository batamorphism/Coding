from collections import deque


# しゃくとり法
def main():
    n = int(input())
    A = list(map(int, input().split()))
    total = sum(A)
    if total % 10 != 0:
        print('No')
        return
    A += A  # 円環はループ

    que = deque()
    siz = 0
    for a in A:
        que.append(a)
        siz += a
        # sizは、totalの10分の1以下
        while que and not (siz <= total//10):
            siz -= que.popleft()
        if siz == total//10:
            print('Yes')
            return
    print('No')


main()
