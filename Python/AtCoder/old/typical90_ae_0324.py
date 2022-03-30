# nim
def main():
    _ = int(input())
    W = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # calc nim
    # nim[w][b] := 白がw個、青がb個あるときのnim
    w_end = 51
    b_end = 51  # bは操作中に増やしていける
    for w in reversed(range(w_end)):
        b_end += w

    nim_of = [[-1]*b_end for _ in range(w_end)]
    # nim = 0だと現在手番の者が敗北確定
    # nim != 0だと常に0にする手が存在するので処理確定
    # w == 0 かつ b <= 1の場合敗北
    nim_of[0][0] = 0
    nim_of[0][1] = 0
    for cur_w in range(w_end):
        for cur_b in range(b_end):
            nim_set = set()
            # 1. 操作Aをやる
            if cur_w >= 1 and (cur_b+cur_w < b_end):
                nex_b = cur_b + cur_w
                nex_w = cur_w - 1
                nim_set.add(nim_of[nex_w][nex_b])
            # 2. 操作Bをやる
            if cur_b >= 2:
                for k in range(1, cur_b//2+1):
                    nex_b = cur_b - k
                    nex_w = cur_w
                    nim_set.add(nim_of[nex_w][nex_b])
            # 3. mexを求める
            for val in range(len(nim_set)+10):
                if val not in nim_set:
                    nim_of[cur_w][cur_b] = val
                    break

    # 各山について、xorを取る
    nim_xor = 0
    for w_i, b_i in zip(W, B):
        nim_xor ^= nim_of[w_i][b_i]
    if nim_xor == 0:
        print('Second')
    else:
        print('First')


main()
