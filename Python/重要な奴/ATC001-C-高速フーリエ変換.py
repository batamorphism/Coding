# 高速フーリエ変換
# i円の主菜がa[i]種類
# j円の副菜がb[j]種類あり
# ちょうどk円になる、主菜と副菜の組み合わせがいくつあるかを調べよ
# ちょうどk円になる組み合わせがc[k]通りとすると、次が成立する
# sum([a[i]*b[k-i] for i in range(k+1)])
# ただし、a[0] = 0とする
# このような処理を畳み込みという
#
# ここで、i次の係数がa[i]である多項式g(x)と
# j次の係数がb[j]である多項式h(x)を考えると
# g(x)*h(x)のk次の係数は、a[i]とb[i]の畳み込みとなっている
# このg(x)*h(x)を求めればよい

import numpy as np


def main():
    n, *ip = map(int, open(0).read().split())

    a = [0]*(n+1)
    b = [0]*(n+1)
    for i in range(1, n+1):
        a[i] = ip[2*(i-1)]
        b[i] = ip[2*(i-1)+1]

    c = convolve(a, b)
    for i in range(1, len(c)):
        print(c[i])


def convolve(f, g):
    """多項式 f, g の積を計算する。

    Parameters
    ----------
    f : np.ndarray (int64)
        f[i] に、x^i の係数が入っている

    g : np.ndarray (int64)
        g[i] に、x^i の係数が入っている


    Returns
    -------
    h : np.ndarray
        f,g の積
    """
    # h の長さ以上の n=2^k を計算
    fft_len = 1
    while 2 * fft_len < len(f) + len(g) - 1:
        fft_len *= 2
    fft_len *= 2

    # フーリエ変換
    Ff = np.fft.rfft(f, fft_len)
    Fg = np.fft.rfft(g, fft_len)

    # 各点積
    Fh = Ff * Fg

    # フーリエ逆変換
    h = np.fft.irfft(Fh, fft_len)

    # 小数になっているので、整数にまるめる
    h = np.rint(h).astype(np.int64)

    return h[:len(f) + len(g) - 1].tolist()


main()
