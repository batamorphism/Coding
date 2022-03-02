# スタックに、書かれている値と、それが何個連続しているかのタプルを置く
def main():
    n = int(input())
    A = list(map(int, input().split()))

    que = [(float('inf'), 0)]
    for a in A:
        last_ball = que[-1]
        last_val, last_cnt = last_ball
        if last_val == a:
            que.append((a, last_cnt+1))
        else:
            que.append((a, 1))
        # kを超えたかの判定
        last_ball = que[-1]
        last_val, last_cnt = last_ball
        if last_val <= last_cnt:
            # last_valじゃなくなるまで、除外し続ける
            while que and not (que[-1][0] != last_val):
                que.pop()
        ans = len(que) - 1
        print(ans)


main()
