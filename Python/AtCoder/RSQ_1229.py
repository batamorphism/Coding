def main():
    n, q = map(int, input().split())

    # setup bit
    bit_end = n + 10
    bit_dat = [0]*bit_end

    def add(pos, val):
        pos += 1
        while pos < bit_end:
            bit_dat[pos] += val
            pos += (pos & -pos)

    def getsum(pos):
        pos += 1
        ret = 0
        while pos > 0:
            ret += bit_dat[pos]
            pos -= (pos & -pos)
        return ret

    ans_list = []
    for _ in range(q):
        com, x, y = map(int, input().split())
        if com == 0:
            add(x, y)
        else:
            ans = getsum(y) - getsum(x-1)
            ans_list.append(ans)

    print(*ans_list, sep='\n')


main()
