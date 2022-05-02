def main():
    n = int(input())
    ALL = 1 << n
    ans_list = []
    for bit in range(ALL):
        stk = []
        for i in range(n):
            if bit >> i & 1:
                stk.append(')')
            else:
                stk.append('(')
        text = ''.join(stk)
        if check(text):
            ans_list.append(text)
    ans_list.sort()
    print(*ans_list, sep='\n')


def check(text):
    # 正しいかっこ列であることを確認
    # 累積和をとり、途中で-1以下にならないこと、最後が0で終わることを見ればよい
    n = len(text)
    arr = []
    for i, c_i in enumerate(text):
        if c_i == '(':
            arr.append(1)
        else:
            arr.append(-1)

    for i in range(1, n):
        arr[i] += arr[i - 1]
    if min(arr) < 0 or arr[-1] != 0:
        return False
    else:
        return True


main()
