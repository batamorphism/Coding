# フィボナッチ数列の和でnを表す
# 3 + [1] + 4 + [2] + 3  + [3] + 4 + [4] ...
# フィボナッチ数列のi番目の要素が必要な場合は
# i個めの3と4の間に挿入する
from audioop import reverse


def main():
    n = int(input())
    fib_end = 10**18+10
    fib_list = []
    pre_fib = 1
    fib = 1
    while fib <= fib_end:
        fib_list.append(fib)
        fib, pre_fib = fib + pre_fib, fib

    use_index_set = set()
    for i in reversed(range(len(fib_list))):
        fib = fib_list[i]
        if n >= fib:
            if i in use_index_set:
                raise
            use_index_set.add(i)
            n -= fib

    ans_list = []
    fib_index = 0
    max_fib_index = max(use_index_set)
    for i in range(999):
        if i % 4 == 0:
            ans_list.append(3)
        elif i % 4 == 2:
            ans_list.append(4)
        elif i % 4 == 1:
            # 操作2を行いたい
            if fib_index in use_index_set:
                ans_list.append(2)
            fib_index += 1
        else:
            # 操作1を行いたい
            if fib_index in use_index_set:
                ans_list.append(1)
            fib_index += 1
        if fib_index > max_fib_index:
            break

    ans_list.reverse()
    print(len(ans_list))
    print(*ans_list, sep='\n')


main()
