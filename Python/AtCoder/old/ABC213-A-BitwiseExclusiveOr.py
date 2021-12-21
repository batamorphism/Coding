# Pythonのxorは^
# 1 = ^^となる
# A ^ C = Bと
# A ^ B = C は同値

def main():
    a, b = map(int, open(0).read().split())
    print(a ^ b)


main()
