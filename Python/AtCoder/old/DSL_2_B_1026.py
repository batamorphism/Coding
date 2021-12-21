bit_end = 10**6
data = [0]*(bit_end+10)


def add(pos, x):
    pos += 1
    while pos < bit_end:
        data[pos] += x
        pos += pos & -pos


def get_sum(pos):
    pos += 1
    ret = 0
    while pos > 0:
        ret += data[pos]
        pos -= pos & -pos
    return ret


def main():
    n, q = map(int, input().split())
    for _ in range(q):
        c, x, y = map(int, input().split())
        if c == 0:
            add(x, y)
        else:
            print(get_sum(y)-get_sum(x-1))


main()
