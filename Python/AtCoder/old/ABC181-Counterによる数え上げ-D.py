from collections import Counter


def main():
    # input
    pre_s = input()
    n = len(pre_s)
    s = []
    for i in range(n):
        s.append(int(pre_s[i]))
    solver(s, n)


def solver(s: list, n: int):
    """solver
    sは1～9のみからなる数字列
    sを並び替えて8の倍数を作れるか
    nは最大で10**5
    8の倍数であるとは
    8*125=1000であるから
    8*1～8*125までの下3桁の組み合わせ125パターンがあるか否かである
    008-0*2,8*1
    016-0*1,1*1,6*1
    024
    ...
    992
    000

    Args:
        s (int): [description]
    """
    ans = 'No'
    if n == 1 and s[0] == 8:
        ans = 'Yes'
    elif n == 2:
        cnt = Counter(s)  # 各要素の出現回数が記録された辞書
        for i in range(8*2, 8*12, 8):
            cnt_of_8 = Counter(list(map(int, str(i))))
            if not(cnt_of_8 - cnt):
                ans = 'Yes'
                break
    else:
        cnt = Counter(s)  # 各要素の出現回数が記録された辞書
        for i in range(13*8, 992, 8):
            cnt_of_8 = Counter(list(map(int, str(i))))
            if not(cnt_of_8 - cnt):
                ans = 'Yes'
                break
    print(ans)


main()