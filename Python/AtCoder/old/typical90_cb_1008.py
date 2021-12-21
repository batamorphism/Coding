def main():
    n, d = map(int, input().split())
    A = list(map(int, input().split()))
    # A[i]とandした結果、0になる個数
    # = 2**[A[i]の0の個数]
    # (A[i] and x) = 0 and (A[j] and x) = 0
    # =(A[i] or A[j]) and x = 0
    # 2**n通りのbit全探索
    ans = 0
    ALL = 1 << n
    for bit in range(ALL):
        if bit == 0:  # Aが1個もない
            continue
        a = 0
        is_add = False
        for i in range(n):
            if bit >> i & 1:
                is_add = not is_add
                a = a | A[i]
        if is_add:
            ans += count_and_x_eq_zero(a, d)
        else:
            ans -= count_and_x_eq_zero(a, d)
    print((1 << d)-ans)


def count_and_x_eq_zero(a: int, d: int) -> int:
    count_zero = d-bin(a)[2:].count('1')
    return 2**count_zero


main()
