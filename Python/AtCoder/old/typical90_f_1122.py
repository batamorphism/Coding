# 辞書順は貪欲に先頭から
# 各文字について、入力文字のi番目以降初めてその文字が出てくるタイミングを記録する
# find_aft[char][i] = i番目以降でcharが初めて出てくるindex
# 0-indexed
# find_aft[char][i] = indとして、残りの文字数はn_end-ind(indを含む)
def char_2_int(char: str):
    return ord(char) - ord('a')


def int_2_char(int_: int):
    return chr(int_ + ord('a'))


def main():
    n_end, k = map(int, input().split())
    S = input()
    A = [char_2_int(c) for c in S]
    char_end = char_2_int('z')+1

    # set find_aft
    INF = 10**9
    find_aft = [[INF]*(n_end+1) for _ in range(char_end)]
    for i in range(n_end-1, -1, -1):
        # まずは、i+1番目の値をコピー
        for char in range(char_end):
            find_aft[char][i] = find_aft[char][i+1]
        a = A[i]
        find_aft[a][i] = i

    ans = []
    ans_ind = 0
    cur_ind = 0

    char = 0
    while True:
        # 残り追加しなくちゃいけない文字数
        remain = k-ans_ind
        char_ind = find_aft[char][cur_ind]
        # charを採用する場合、char込みで使える文字数は
        # n_end-char_ind
        if n_end-char_ind >= remain:
            # charを採用可能
            ans_ind += 1
            cur_ind = char_ind + 1
            ans.append(char)
            if ans_ind == k:
                # print('ok')
                break
            # print(char, ans_ind, cur_ind, [int_2_char(c) for c in ans])
            char = 0  # aに戻る
        else:
            char += 1

    ans = [int_2_char(c) for c in ans]
    print(''.join(ans))


main()
