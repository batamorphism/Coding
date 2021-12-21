from collections import deque

# BIT
Data = [0]*(10**5+20)
Bit_max = 10**5+10


def add(pos, x):
    pos += 1
    while pos < Bit_max:
        Data[pos] += x
        pos += pos & -pos


def getsum(pos):
    # pos以下の合計
    pos += 1
    ret = 0
    while pos > 0:
        ret += Data[pos]
        pos -= pos & -pos
    return ret


def main():
    _ = int(input())
    que = deque()
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        que.append(a)
        # aがqueの最大値(重複なし)であればTrue
        # すなわち、a-1以下の個数がlen(que)-1ならTrue
        add(a, 1)
        while que and not (getsum(a-1) == len(que)-1):
            rm = que.popleft()
            add(rm, -1)
        ans += len(que)

    print(ans)


main()
