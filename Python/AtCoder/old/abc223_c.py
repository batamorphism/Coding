from collections import deque


def main():
    n = int(input())
    que = deque()
    for _ in range(n):
        a, b = map(int, input().split())
        c = a/b
        que.append((a, b, c))

    if n == 1:
        a, b, c = que.pop()
        print(a/2)
        return
    ans = 0
    le = que.popleft()
    ri = que.pop()
    le_a, le_b, le_c = le
    ri_a, ri_b, ri_c = ri
    while que:
        if le_c < ri_c:
            # 左が先に燃え尽きる
            ans += le_c*le_b
            ri_c = ri_c-le_c
            le = que.popleft()
            le_a, le_b, le_c = le
        else:
            # 右が先に燃え尽きる
            ans += ri_c*le_b
            le_c = le_c - ri_c
            ri = que.pop()
            ri_a, ri_b, ri_c = ri
    # 残り、riとleのみ残っている状態
    if le_c < ri_c:
        # 左が先に燃え尽きる
        ans += le_c*le_b
        ri_c = ri_c-le_c
        ans += ri_c*ri_b/2
    else:
        # 右が先に燃え尽きる
        ans += ri_c*le_b
        le_c = le_c - ri_c
        ans += le_c*le_b/2
    print(ans)


main()
