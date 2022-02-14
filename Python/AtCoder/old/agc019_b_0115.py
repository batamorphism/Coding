from collections import Counter


# 同じ文字が出てくると、その組み合わせ分だけ減ってしまう
# 全てが違う文字の場合、n*(n-1)//2+1通り存在
def main():
    A = list(input())
    n = len(A)
    cnt_of = Counter(A)
    total = n*(n-1)//2 + 1
    for key, cnt in cnt_of.items():
        total -= cnt*(cnt-1)//2
    print(total)


main()
