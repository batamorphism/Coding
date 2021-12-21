from collections import deque

bit_end = 10**5+1
bit_data = [0]*bit_end


def add(pos, x):
    while pos < bit_end:
        bit_data[pos] += x
        pos += pos & -pos


def getsum(pos):
    s = 0
    while pos > 0:
        s += bit_data[pos]
        pos -= pos & -pos
    return s


def main():
    n = int(input())
    A = list(map(int, input().split()))
    que = deque()
    ans = 0
    for a in A:
        que.append(a)
        add(a, 1)
        while que and not getsum(a-1) == len(que)-1:
            rm = que.popleft()
            add(rm, -1)
        ans += len(que)

    print(ans)


main()
