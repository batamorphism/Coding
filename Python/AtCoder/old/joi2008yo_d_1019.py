def main():
    m = int(input())
    A = [tuple(map(int, input().split())) for _ in range(m)]
    n = int(input())
    B = set([tuple(map(int, input().split())) for _ in range(n)])
    a0_x, a0_y = A[0]
    for b_x, b_y in B:
        offset_x = b_x-a0_x
        offset_y = b_y-a0_y
        collect = True
        for a_x, a_y in A:
            if (a_x+offset_x, a_y+offset_y) not in B:
                collect = False
                break
        if collect:
            print(offset_x, offset_y)
            return


main()
