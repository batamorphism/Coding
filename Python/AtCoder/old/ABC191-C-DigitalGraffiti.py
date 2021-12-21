# ###
#  ##
#   #
# これは、8角形

def main():
    h, w = map(int, input().split())
    S = []
    for _ in range(w):
        S.append(list(input()))
    p_list(S)

def p_list(pl: list):
    for s in pl:
        print(s)

main()