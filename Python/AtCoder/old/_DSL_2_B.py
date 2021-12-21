def main():
    n, q = map(int, input().split())
    BIT = [0]*(n+10)

    def add(pos, x):
        pos += 1
        while pos <= n:
            BIT[pos] += x
            pos += pos & -pos

    def get_sum(pos):
        pos += 1
        ret = 0
        while pos > 0:
            ret += BIT[pos]
            pos -= pos & -pos
        return ret

    for _ in range(q):
        com, x, y = map(int, input().split())
        if com == 0:
            pos = x-1
            add(pos, y)
        else:
            pos1 = x-1
            pos2 = y-1
            if pos1 >= 0:
                ans = get_sum(pos2)-get_sum(pos1-1)
            else:
                ans = get_sum(pos2)
            print(ans)


main()
