def main():
    n = int(input())
    s = input()
    q = int(input())
    T = []
    A = []
    B = []
    for _ in range(q):
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)

    s_bef = list(s[:n])
    s_aft = list(s[n:])
    is_swapped = False
    for i in range(q):
        if T[i] == 1:
            # Sのa文字目とb文字目を入れ替える
            a = A[i]
            b = B[i]
            if not is_swapped:
                if a<=n:
                    aa = a-1
                    a_swap_char = s_bef[aa]
                else:
                    aa = a-n-1
                    a_swap_char = s_aft[aa]
                if b<=n:
                    bb = b-1
                    b_swap_char = s_bef[bb]
                    s_bef[bb] = a_swap_char
                else:
                    bb = b-n-1
                    b_swap_char = s_aft[bb]
                    s_aft[bb] = a_swap_char
                if a<=n:
                    s_bef[aa] = b_swap_char
                else:
                    s_aft[aa] = b_swap_char
            else:
                if a<=n:
                    aa = a-1
                    a_swap_char = s_aft[aa]
                else:
                    aa = a-n-1
                    a_swap_char = s_bef[aa]
                if b<=n:
                    bb = b-1
                    b_swap_char = s_aft[bb]
                    s_aft[bb] = a_swap_char
                else:
                    bb = b-n-1
                    b_swap_char = s_bef[bb]
                    s_bef[bb] = a_swap_char
                if a<=n:
                    s_aft[aa] = b_swap_char
                else:
                    s_bef[aa] = b_swap_char
        else:
            is_swapped = not is_swapped

    if not is_swapped:
        ans = ''.join(s_bef+s_aft)
    else:
        ans = ''.join(s_aft+s_bef)
    print(ans)


main()
