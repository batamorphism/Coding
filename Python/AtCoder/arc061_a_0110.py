# a+b -> a b +
# a x b + c -> a b x c +
# a x b + c x d -> a b x c d x +
# a b x c d + x -> a x b x (c + d) だめ
# もう実直にやる
def main():
    S = list(map(int, list(input())))
    n = len(S)
    n = 2*n - 1
    # 0, 2, 4,...に数字が入る
    # 1, 3, 5,...に記号が入る
    A = []
    symbol_pos = []
    for i in range(n):
        if i % 2 == 0:
            A.append(S[i//2])
        else:
            A.append('*')
            symbol_pos.append(i)

    # print(A)
    # print(symbol_pos)
    symbol_cnt = len(symbol_pos)
    ALL = 1 << symbol_cnt
    ans = 0
    for bit in range(ALL):
        for i in range(symbol_cnt):
            if bit >> i & 1:
                A[2*i+1] = '+'
            else:
                A[2*i+1] = 'x'
        val = calc(A)
        # print(A, val)
        ans += val

    print(ans)


def calc(A):
    value_list = []
    val = 0
    for a in A:
        if a == '+':
            value_list.append(val)
            val = 0
        elif a == 'x':
            val *= 10
        else:
            val += a
    value_list.append(val)
    return sum(value_list)


main()
