# 各頂点に対し、自分より小さい隣接頂点の数を数えていく1
def main():
    node_end, edge_end = map(int, input().split())

    cnt_lower_of = [0]*node_end
    for _ in range(edge_end):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if a > b:
            a, b = b, a
        # a < b
        cnt_lower_of[b] += 1

    ans = sum(1 for i in cnt_lower_of if i == 1)
    print(ans)


main()
