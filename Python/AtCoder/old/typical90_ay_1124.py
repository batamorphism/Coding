# 半分全列挙
def main():
    n, k, p = map(int, input().split())
    A = list(map(int, input().split()))

    A1 = A[:n//2]
    A2 = A[n//2:]

    # Aについて、
    # A[cnt] = cnt個を選んで合計val円となる
    # リストを作成する
    pattern_list1 = [[] for _ in range(41)]
    pattern_list2 = [[] for _ in range(41)]

    def set_pattern(pattern_list, A):
        bit_all = 1 << len(A)
        a_end = len(A)
        for bit in range(bit_all):
            cnt = 0
            val = 0
            for a_i in range(a_end):
                if (bit >> a_i) & 1:
                    cnt += 1
                    val += A[a_i]
            pattern_list[cnt].append(val)
        return

    set_pattern(pattern_list1, A1)
    set_pattern(pattern_list2, A2)

    for val_list in pattern_list1:
        val_list.sort()

    for val_list in pattern_list2:
        val_list.sort()

    ans = 0
    for cnt1, val1_list in enumerate(pattern_list1):
        cnt2 = k-cnt1
        if cnt2 < 0:  # ここの打ち切りが重要
            break
        for val1 in val1_list:  # ここでキャッシュメモリにval1_listが入る
            val2_max = p - val1
            if val2_max < 0:  # ここの打ち切りが重要
                break
            val2_list = pattern_list2[cnt2]
            ok = -1
            ng = len(val2_list)
            while ng-ok > 1:
                mid = (ok+ng)//2
                if val2_list[mid] <= val2_max:
                    ok = mid
                else:
                    ng = mid
            ans += ok+1

    print(ans)


main()
