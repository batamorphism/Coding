def main():
    r_cnt, c_cnt, n = map(int, input().split())
    card_r = []
    card_c = []
    for _ in range(n):
        r, c = map(int, input().split())
        card_r.append(r)
        card_c.append(c)

    # sortしてdictに入れる
    dict_r = {}
    dict_c = {}
    # dict_r[card_r] = 何番目か
    sorted_card_r = sorted(set(card_r))
    for i, card in enumerate(sorted_card_r):
        dict_r[card] = i+1
    sorted_card_c = sorted(set(card_c))
    for i, card in enumerate(sorted_card_c):
        dict_c[card] = i+1

    for card in zip(card_r, card_c):
        r, c = card
        print(dict_r[r], dict_c[c])


main()
