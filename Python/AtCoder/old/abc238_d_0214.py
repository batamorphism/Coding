# x+y = x^y + 2*(x&y)
# a = x&y
# x+y = s
# ゆえに
# s = x^y + 2*a
# a = x&y
# ゆえに
# s-2*a = x^y
# a = x&y
# ここで
# x  |0101
# y  |0011
# x^y|0110
# x&y|0001
# よって、(x^y)&(x&y)=0であれば十分
def main():
    t = int(input())
    for _ in range(t):
        a, s = map(int, input().split())
        xor_ = s-2*a
        and_ = a
        if xor_ < 0:
            print('No')
            continue
        if xor_ & and_ == 0:
            print('Yes')
        else:
            print('No')


main()

