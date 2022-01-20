# pos[i][c] Sのi番目以降の文字でcが出現する場所
from collections import defaultdict
import string


def main():
    n, k = map(int, input().split())
    S = ['*'] + list(input())

    pos = defaultdict(lambda: defaultdict(lambda: -1))
    for i in reversed(range(n+1)):
        s_i = S[i]
        pos[i][s_i] = i
        for c in string.ascii_lowercase:
            if c != s_i:
                pos[i][c] = pos[i + 1][c]

    """
    print(pos[1]['a']) -> 1
    print(pos[2]['a']) -> -1
    """

    ans = []
    i = 1
    while len(ans) < k:
        for c in string.ascii_lowercase:
            # cがansに追加しうるか確認する
            # Sのi番目以降の文字でcが出現する場所
            c_ind = pos[i][c]
            if c_ind == -1:
                continue
            if n - c_ind + 1 < k - len(ans):
                # cを採用した場合、後n-c_ind+1文字しか追加できない
                continue
            ans.append(c)
            i = c_ind + 1
            break

    print(''.join(ans))


main()
