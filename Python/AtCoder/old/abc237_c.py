# 末尾のaを消していく
# 全てaの時はTrue
# 先頭から数えた、連続するaの個数分だけ残して、末尾のaを消す
from collections import Counter


def main():
    S = input()
    S = list(S)

    # check_all_a
    cnt_of = Counter(S)
    if cnt_of['a'] == len(S):
        print('Yes')
        return

    front_a = 0
    back_a = 0
    for c in S:
        if c == 'a':
            front_a += 1
        else:
            break
    for c in reversed(S):
        if c == 'a':
            back_a += 1
        else:
            break

    # もし、front_a > back_a ならば、回文にならない
    if front_a > back_a:
        print('No')
        return

    # それ以外は、aがないものとして扱ってよい
    new_S = S[front_a:len(S)-back_a]
    reversed_new_S = list(reversed(new_S))
    if new_S == reversed_new_S:
        print('Yes')
    else:
        print('No')


main()
