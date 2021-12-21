def main():
    n, q = map(int, input().split())
    Max_Data = n+10
    Data = [0] * (Max_Data+10)

    def add(pos, x):
        pos += 1
        while pos < Max_Data:
            Data[pos] += x
            pos += pos & -pos

    def get_sum(pos):
        pos += 1
        ret = 0
        while pos > 0:
            ret += Data[pos]
            pos -= pos & -pos
        return ret

    for _ in range(q):
        c, x, y = map(int, input().split())
        if c == 0:
            x -= 1
            add(x, y)
        else:
            x -= 1
            y -= 1
            print(get_sum(y)-get_sum(x-1))


main()

