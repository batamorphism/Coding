# バックトラック?
import sys
sys.setrecursionlimit(10 ** 6)
ans = 0


def main():
    n, x = map(int, input().split())
    balls_list = []
    for _ in range(n):
        _, *balls = map(int, input().split())
        balls = list(balls)
        balls_list.append(balls)

    # print(balls_list)
    def dfs(pre_cnt, pre_prod):
        # cnt個のボールを取った状態で、ボールの総積がpre_prodになっている
        if pre_cnt == n:
            if pre_prod == x:
                global ans
                ans += 1
            return
        cur_cnt = pre_cnt + 1
        cur_balls = balls_list[cur_cnt - 1]
        for ball in cur_balls:
            cur_prod = pre_prod * ball
            if cur_prod > x:
                continue
            if x % cur_prod != 0:
                continue
            dfs(cur_cnt, pre_prod * ball)

    dfs(0, 1)
    print(ans)


main()
