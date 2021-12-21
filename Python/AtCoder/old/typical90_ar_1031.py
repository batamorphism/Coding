def main():
    n, q_end = map(int, input().split())
    A = list(map(int, input().split()))
    q_list = []
    for _ in range(q_end):
        t, x, y = map(int, input().split())
        x -= 1
        y -= 1
        q_list.append((t, x, y))

    # Aを円環で考える
    st = 0
    mod = len(A)
    for q in q_list:
        t, x, y = q
        if t == 1:
            x += st
            y += st
            x %= mod
            y %= mod
            A[x], A[y] = A[y], A[x]
            # print(A)
        elif t == 2:
            st -= 1
            st %= mod
        else:
            x += st
            x %= mod
            print(A[x])


main()
