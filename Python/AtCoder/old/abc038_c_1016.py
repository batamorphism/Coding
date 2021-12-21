from collections import deque

bit_max = 10**5+10
data = [0]*(bit_max+10)


def add(pos, x):
    pos += 1
    while pos < bit_max:
        data[pos] += x
        pos += pos & -pos


def getsum(pos):
    pos += 1
    ret = 0
    while pos > 0:
        ret += data[pos]
        pos -= pos & -pos
    return ret


def main():
    n = int(input())
    A = list(map(int, input().split()))
    que = deque()
    ans = 0
    for a in A:
        que.append(a)
        add(a, 1)
        while que and not len(que) == getsum(a-1)+1:
            rm = que.popleft()
            add(rm, -1)
        ans += len(que)
    print(ans)


main()
