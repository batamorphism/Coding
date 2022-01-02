from collections import defaultdict


# 一番安い街で買って、一番高い街で売る
# したがって、一番安い街と一番高い街以外、存在意義がない
# 最安値が更新されるたびに、min_aを小さくし、max_aをmin_aと同じにする
# max_aは都度新しくしていく
# max_a-min_aのペアが重要
def main():
    n, t = map(int, input().split())
    A = list(map(int, input().split()))
    INF = float('inf')
    min_a = (INF, -1)
    max_a = (-INF, -1)
    d = defaultdict(list)

    max_ans = -INF
    for i, a in enumerate(A):
        if a < min_a[0]:
            min_a = (a, i)
            max_a = (a, i)
        else:
            if a > max_a[0]:
                max_a = (a, i)
        ans = a - min_a[0]
        max_ans = max(max_ans, ans)
        # max_ansを満たすindexのペアを保持する
        d[ans].append((min_a[1], i))

    need_pair_list = d[max_ans]
    # need_pairについて、1円変更する必要がある・・・
    # 挟まれてると・・・だめ?
    # 
    print(len(need_pair_list))


main()
