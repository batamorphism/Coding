def main():
    # dequeを、バッファーで実装
    n, q = map(int, input().split())
    deque = [-1]*(2*n+10)
    le = n+1
    ri = n+1
    # [le, ri)で管理する
    A = list(map(int, input().split()))
    for i, a in enumerate(A):
        deque[ri] = a
        ri += 1

    ans_list = []

    for _ in range(q):
        t, x, y = map(int, input().split())
        if t == 1:
            # swap
            x -= 1
            y -= 1
            x += le
            y += le
            deque[x], deque[y] = deque[y], deque[x]
        if t == 2:
            # shift
            a_ri = deque[ri-1]
            deque[le-1] = a_ri
            deque[ri-1] = -1
            le -= 1
            ri -= 1
        if t == 3:
            # get
            x -= 1
            x += le
            ans_list.append(deque[x])
        # print(deque)

    print(*ans_list, sep='\n')


main()
