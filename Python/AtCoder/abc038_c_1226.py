from collections import deque


def main():
    n = int(input())
    A = list(map(int, input().split()))

    que = deque()
    # 単調増加かどうかは
    # 新たに足したaがその一個前のaよりも大きいかどうかで判定できる
    last_a = -float('inf')
    ans = 0
    for a in A:
        if last_a < a:
            is_increasing = True
        else:
            is_increasing = False
        que.append(a)
        last_a = a
        while que and not is_increasing:
            # remove all
            que = deque()
            que.append(a)
            is_increasing = True
        ans += len(que)
    print(ans)


main()
