from collections import Counter


def main():
    A = input()
    # 同じ文字が出ると、一回減る
    # Aの各文字の出現スウを数え
    # 同じ文字の選び方だけ、組み合わせ数を減らす
    n = len(A)
    total = n*(n-1)//2 + 1

    cnt_of = Counter(A)

    for key, val in cnt_of.items():
        comp = val*(val-1)//2
        total -= comp

    print(total)


main()
