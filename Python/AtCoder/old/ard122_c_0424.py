# ...4343の操作を繰り返していき、間に挿入していく
def main():
    n = int(input())
    # n以下のフィボナッチ数列を求める。
    fib = create_fib(n)

    # nを作るために必要なフィボナッチ数列の部分列を求める
    cur_n = n
    need_list = []
    for i in reversed(range(len(fib))):
        f_i = fib[i]
        while f_i <= cur_n:
            cur_n -= f_i
            need_list.append((i, f_i))

    need_list.sort(reverse=True)
    ans = []
    cur_ind = need_list[0][0]
    need_set = set([i for i, _ in need_list])
    while cur_ind > 0:
        if cur_ind in need_set:
            # このフィボナッチ数は必要
            if cur_ind % 2 == 0:  # 偶数の時は、操作1を行う
                ans.append(1)
            else:  # 奇数の時は、操作2を行う
                ans.append(2)
        # 常に、操作3か4は行う
        if cur_ind % 2 == 0:
            ans.append(4)
        else:
            ans.append(3)
        cur_ind -= 1

    print(len(ans))
    print(*ans)


def create_fib(n):
    fib = [1, 1]
    while True:
        pre1 = fib[-1]
        pre2 = fib[-2]
        cur = pre1 + pre2
        fib.append(cur)
        if cur > n:
            return fib


main()
