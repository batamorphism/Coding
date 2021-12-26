import string


def main():
    S = input()
    T = input()
    # SとTを数列に変換する
    abc = list(string.ascii_lowercase)
    S_list = [abc.index(s) for s in S]
    T_list = [abc.index(t) for t in T]

    delta_list = []
    mod = len(abc)
    for i, s in enumerate(S_list):
        t = T_list[i]
        delta = (s-t) % mod
        delta_list.append(delta)

    num_0 = delta_list[0]
    for num in delta_list:
        if num != num_0:
            print('No')
            return
    print('Yes')


main()
