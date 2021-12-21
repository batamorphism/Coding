def main():
    n = int(input())
    # 高度が高い順に風船を割っていく
    target_list = [list(map(int, input().split())) for _ in range(n)]
    # 最大値は、10**9が10**5回繰り返される
    ok = 10**16
    ng = 0
    while ok-ng > 1:
        mid = (ok+ng)//2
        if check(target_list, mid):
            ok = mid
        else:
            ng = mid
    print(ok)


def check(target_list, x):
    # ペナルティx以下で全てを割ることができるか
    # 各targetに対し、何回以内に割らないといけないか
    max_time_list = []
    for h, s in target_list:
        max_time_list.append((x-h)//s)
    max_time_list.sort()
    for i, time in enumerate(max_time_list):
        if i > time:
            # その時割った時刻が実際に割った時刻を超えている
            return False
    return True


main()
