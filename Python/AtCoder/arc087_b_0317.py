from collections import defaultdict
import copy


# xy独立に考える
def main():
    S = input() + 'T'
    en_x, en_y = map(int, input().split())

    command_list_x = []
    command_list_y = []
    val = 0
    is_x = True
    is_first = True
    for c in S:
        if c == 'F':
            val += 1
        else:
            if is_x:
                if is_first:
                    command = (val,)
                else:
                    command = (val, -val)
                command_list_x.append(command)
            else:
                command = (val, -val)
                command_list_y.append(command)
            val = 0
            is_first = False
            is_x = not is_x

    ans1 = solve(command_list_x, en_x)
    ans2 = solve(command_list_y, en_y)
    ans = ans1 and ans2
    if ans:
        print('Yes')
    else:
        print('No')


def solve(command_list, en_x):
    # command_listを組み合わせて、最後にen_xにいることができるか
    # 配るDP
    dp = set([0])
    for command in command_list:
        new_dp = set()
        for pre in dp:
            for val in command:
                cur = pre+val
                new_dp.add(cur)
        dp = copy.deepcopy(new_dp)
    return en_x in dp


main()
