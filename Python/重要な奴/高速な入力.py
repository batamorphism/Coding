import sys


def main():
    read = sys.stdin.buffer.read
    # Ctrl+Zで入力終了
    # 全部が数値の時はうまくいくけど、そうでないときは改行が入るので注意
    data = list(map(int, read().split()))
    print(data)


main()
