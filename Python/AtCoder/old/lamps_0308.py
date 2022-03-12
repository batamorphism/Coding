def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    bef_A = A
    for _ in range(k):
        aft_A = one_step(bef_A)
        if aft_A == bef_A:
            break
        bef_A = aft_A
    print(*aft_A)


def one_step(A):
    n = len(A)
    ret = [0] * n
    # imos
    for x, a_x in enumerate(A):
        # [x-a_x, x+a_x]に+1する
        lo = max(0, x-a_x)
        hi = min(n, x+a_x+1)
        ret[lo] += 1
        if hi < n:
            ret[hi] -= 1

    for i in range(1, n):
        ret[i] += ret[i-1]
    return ret


main()
