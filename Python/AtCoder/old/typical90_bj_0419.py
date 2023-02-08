# 後ろから見る
def main():
    node_end = int(input())
    item_list = []
    for i in range(node_end):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        item_list.append((a, b))

    # item_list[i] = a_i, b_iとして
    # a_iかb_iが白ならば、iを黒にできる
    # 逆の操作を考えると、iを黒から白に戻すためには、a_iかb_iが白であればよい
    # したがって、a_i -> i , b_i -> i のedgeを張り
    # 全体を尽くせればok

    nei_of = [[] for _ in range(node_end)]
    for i, (a_i, b_i) in enumerate(item_list):
        nei_of[a_i].append(i)
        nei_of[b_i].append(i)

    stk = []
    ans = []
    for i, (a_i, b_i) in enumerate(item_list):
        if a_i == i or b_i == i:
            stk.append(i)

    used = [False] * node_end
    while stk:
        pre = stk.pop()
        if used[pre]:
            continue
        used[pre] = True
        ans.append(pre)
        for cur in nei_of[pre]:
            if used[cur]:
                continue
            stk.append(cur)

    if len(ans) != node_end:
        print(-1)
        return

    for i in reversed(ans):
        print(i+1)


main()
