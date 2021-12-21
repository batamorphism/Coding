# 一番近いクラスに入ればよい
# loで最も近いクラスと、hiで最も近いクラスの距離を求め
# 近いほうに入ればいい
def main():
    INF = float('inf')
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    B = [int(input()) for _ in range(q)]

    AB = []
    for i, a in enumerate(A):
        AB.append((a, 0, i))
    for i, b in enumerate(B):
        AB.append((b, 1, i))

    AB.sort()

    bef_val = INF
    score_list = [INF]*q
    for ab in AB:
        if ab[1] == 0:
            bef_val = ab[0]
        if ab[1] == 1:
            score = abs(ab[0] - bef_val)
            ind = ab[2]
            score_list[ind] = min(score_list[ind], score)

    bef_val = INF
    for ab in AB[::-1]:
        if ab[1] == 0:
            bef_val = ab[0]
        if ab[1] == 1:
            score = abs(ab[0] - bef_val)
            ind = ab[2]
            score_list[ind] = min(score_list[ind], score)

    for score in score_list:
        print(score)


main()
