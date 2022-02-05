def main():
    n, k = map(int, input().split())
    n = str(n)
    for _ in range(k):
        n = one_step(n)
    print(n)


def one_step(n):
    # nは8進法で書かれた文字列
    # それを8進法で整数に読み替える
    # それを9進法の数値に変換し
    # それを9進法の数値のまま文字列に戻し
    # 8を5に書き換える
    n_value = int(n, 8)
    n = convert_9(n_value)
    n = n.replace('8', '5')
    return n


def convert_9(n):
    # 整数nを9進法の文字列に変換する
    ret = []
    while n:
        ret.append(n % 9)
        n //= 9
    if ret:
        return ''.join(map(str, reversed(ret)))
    else:
        return '0'


main()
