def main():
    n = int(input())
    # nを表すfibonacci数列を求める
    fib = [1, 1]
    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])

    use_fib = {}
    cur_val = n
    max_i = -1
    for i in reversed(range(len(fib))):
        fib_i = fib[i]
        if cur_val >= fib_i:
            use_fib[i] = fib_i
            cur_val -= fib_i
            max_i = max(max_i, i)
    if cur_val != 0:
        raise

    ans_list = [3]
    for i in range(1, max_i+1):
        # 奇数回目の操作は操作1、偶数回目の操作は操作2
        is_1 = (i % 2 == 0)
        is_4 = not is_1
        if i in use_fib:
            if is_1:
                ans_list.append(1)
            else:
                ans_list.append(2)
        if is_4:
            ans_list.append(4)
        else:
            ans_list.append(3)
    ans_list = ans_list[::-1]
    print(len(ans_list))
    print(*ans_list, sep='\n')


main()
