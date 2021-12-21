# grundy数
# w, b = 50, 50 からスタートすると
# ope_aを行うたびに、bは+50, +49, ... +1され
# 最大のbは50 + (50+1)*50//2=1325

# grundy[w][b]
def main():
    # set up grundy number
    grundy = [[-1]*1326 for _ in range(51)]
    # w == 0 かつ b <= 1となると負け
    grundy[0][0] = 0
    grundy[0][1] = 0

    for w in range(51):
        for b in range(1326):
            # Aを選んだあとのgrundy数の集合と
            # Bを選んだあとのgrundy数の集合の和を求める
            nex_grundy_set = set()
            if w >= 1:
                # Aを選べるとき
                if b+w <= 1325:
                    nex_grundy = grundy[w-1][b+w]
                    nex_grundy_set.add(nex_grundy)
            if b >= 2:
                # Bを選べるとき
                for k in range(1, b//2+1):
                    nex_grundy = grundy[w][b-k]
                    nex_grundy_set.add(nex_grundy)
            for mex in range(1326):
                if mex not in nex_grundy_set:
                    break
            grundy[w][b] = mex

    _ = int(input())
    W = list(map(int, input().split()))
    B = list(map(int, input().split()))
    g = 0
    for w, b in zip(W, B):
        g ^= grundy[w][b]

    if g == 0:
        print('Second')
    else:
        print('First')


main()
