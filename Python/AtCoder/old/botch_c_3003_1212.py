# g -> 0
# c -> 1
# p -> 2
# a_i - b_i % 3 == 1 -> aの負け
# a_i - b_i % 3 == 2 -> bの負け
# a_i - b_i % 3 == 0 -> あいこ
def main():
    n = int(input())
    gcp_to_int = {'g': 0, 'c': 1, 'p': 2}
    AB = []
    for _ in range(n):
        a, b = input().split()
        a = gcp_to_int[a]
        b = gcp_to_int[b]
        AB.append((a, b))

    cnt_a = 0
    cnt_b = 0

    def judge(a, b):
        # 'a, 'b'のうち勝った方を返す
        # あいこのときは'-'を返す
        if (a - b) % 3 == 1:
            return 'b'
        elif (a - b) % 3 == 2:
            return 'a'
        else:
            return '-'

    for a, b in AB:
        winner = judge(a, b)
        if winner == 'a':
            cnt_a += 1
        elif winner == 'b':
            cnt_b += 1

    print(cnt_a)
    print(cnt_b)


main()
