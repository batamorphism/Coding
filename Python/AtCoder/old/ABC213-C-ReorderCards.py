# 行、列共に、n個の中からソートした時の

def main():
    h, w, n, *pre_AB = map(int, open(0).read().split())
    AB = [[pre_AB[2*i], pre_AB[2*i+1], i] for i in range(n)]
    A = [[AB[i][0], i] for i in range(n)]
    B = [[AB[i][1], i] for i in range(n)]
    A.sort()
    B.sort()

    row = 0
    pre = -1
    cards_row = [0] * n
    for a in A:
        if pre != a[0]:
            row += 1
        cards_row[a[1]] = row
        pre = a[0]

    h = 0
    pre = -1
    cards_h = [0] * n
    for b in B:
        if pre != b[0]:
            h += 1
        cards_h[b[1]] = h
        pre = b[0]

    for i in range(n):
        print(str(cards_row[i]) + ' ' + str(cards_h[i]))


main()
