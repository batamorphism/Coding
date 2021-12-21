def is_correct(arr):
    stack = []
    for a in arr:
        if a == '(':
            stack.append(a)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


def main():
    n_end = int(input())
    # 2**nとおりの(と)の組み合わせをすべて作り
    # 正しいかっこ列である場合のみ、答えに追加
    ans_list = []
    ALL = 1 << n_end
    for bit in range(ALL):
        arr = []
        for n in range(n_end):
            if bit & (1 << n):
                arr.append('(')
            else:
                arr.append(')')
        if is_correct(arr):
            ans_list.append(''.join(arr))

    ans_list.sort()
    print(*ans_list, sep='\n')


main()
