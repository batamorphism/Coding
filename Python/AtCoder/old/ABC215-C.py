import itertools


def main():
    s, s2 = input().split()
    k = int(s2)
    # 全パターンやる
    s_list = list(s)
    perm = list(set(itertools.permutations(s_list)))
    perm.sort()
    str = ''
    str = str.join(perm[k-1])
    print(str)


main()