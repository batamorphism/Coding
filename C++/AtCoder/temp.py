import random
import time
import copy

N = 10

# boxの状態から、f番目の空き位置がどの座標に位置するのか判断
def convert_ft_to_Coordinate(f,box):
    i = 0
    f_tmp = f
    f_tmp_after = f
    while (f_tmp_after > 0) and (i < N-1) :
        # この行にcandyが何個あるか0
        n_row = sum([sum(box[i][j]) for j in range(N)])
        void_row = N - n_row

        # この行を飛ばした場合、残り何番になるか
        f_tmp_after = f_tmp - void_row
        if f_tmp_after > 0 :
            f_tmp = f_tmp - void_row
            i += 1

    # ここで、f_tmp_after < 1, f_tmp > 0 となるので、この行iにcandy入る
    j = 0
    while f_tmp > 1:
        # i,jにキャンディーがあった場合、飛ばす
        if sum(box[i][j]) == 1:
            j += 1
        # candyがない場合、f_tmpを1つ減らし、jを増やす
        else :
            f_tmp -= 1
            j += 1
    # f_tmp = 1となった(次に当たる空部屋にcandyが入る)
    while sum(box[i][j]) == 1:
        j+= 1
    return i,j

# boxを傾ける
def tilt_box(dir, box):
    box_copy = copy.copy(box)

    # 上に落ちてくるときの処理
    if dir == 'F':
        for i in range(N):  # 行
            for j in range(N):  # 列
                # i,jにキャンディーがあれば飛ばす
                # なければ、下方向を参照し、一つでもあればこのマスに持ってくる（持ってきた元のマスは0になる）
                if sum(box_copy[i][j]) > 0 :
                    pass
                else:
                    for k in range(i+1, N):  # 行
                        # i,jにcandyがなく、k,jにcandyがあった場合、このマスに持ってくる(kはiの下側)
                        if sum(box_copy[i][j]) > 0 :pass
                        elif sum(box_copy[k][j]) >0 :
                            box_copy[i][j] = box_copy[k][j]
                            box_copy[k][j] = (0,0,0)  # immutable
                            break
    elif dir == 'L':
        for i in range(N):
            for j in range(N):
                # i,jにキャンディーがあれば飛ばす
                # なければ、右方向を参照し、一つでもあればこのマスに持ってくる（持ってきた元のマスは0になる）
                if sum(box_copy[i][j]) > 0 :
                    pass
                else : 
                    for k in range(j+1, N):
                        # i,jにcandyがなく、i,kにcandyがあった場合、このマスに持ってくる
                        if sum(box_copy[i][j]) > 0 :pass
                        elif sum(box_copy[i][k]) == 1:
                            box_copy[i][j] = copy.copy(box_copy[i][k])
                            box_copy[i][k] = [0,0,0]
                            break
            
    elif dir == 'B':
        for i in range(N-1,-1,-1):
            # 下から順にみていきたい
            for j in range(N):
                # i_,jにキャンディーがあれば飛ばす
                # なければ、上方向を参照し、一つでもあればこのマスに持ってくる（持ってきた元のマスは0になる）
                if sum(box_copy[i][j]) > 0 :
                    pass
                else : 
                    for k in range(i-1,-1,-1):
                        # i_,jにcandyがなく、k,jにcandyがあった場合、このマスに持ってくる(kはiより上)
                        if sum(box_copy[i][j]) > 0 :pass
                        elif sum(box_copy[k][j]) == 1:
                            box_copy[i][j] = copy.copy(box_copy[k][j])
                            box_copy[k][j] = [0,0,0]
                            break
                            
    elif dir == 'R':
        for i in range(N):
            for j in range(N-1,-1,-1):
                # i,j_にキャンディーがあれば飛ばす
                # なければ、左方向を参照し、一つでもあればこのマスに持ってくる（持ってきた元のマスは0になる）
                if sum(box_copy[i][j]) > 0 :
                    pass
                else : 
                    for k in range(j-1,-1,-1):
                        # N-i,jにcandyがなく、i+k,jにcandyがあった場合、このマスに持ってくる
                        if sum(box_copy[i][j]) > 0 :pass
                        elif sum(box_copy[i][k]) == 1:
                            box_copy[i][j] = copy.copy(box_copy[i][k])
                            box_copy[i][k] = [0,0,0]
                            break

    return box_copy
                
    
# score計算
def calc_score(box):
    box_copy = copy.copy(box)
    links = copy.copy(box)
    for i in range(1,N):
        for j in range(1,N):
            # 左、上に同じ種類があれば、score計算
            if sum(box_copy[i][j]) == 1:
                kind = box_copy[i][j].index(1)
                links[i][j][kind] = 1 + links[i-1][j][kind] + links[i][j-1][kind]
    
    # 正確なスコア計算がしたいけど出来ないので、以下近似
    # 種別ごとの最大連結を計算、その二乗の和をスコアとする
    max_links =  [0,0,0]
    for k in range(3):
        for i in range(N):
            for j in range(N):
                cont = links[i][j][k]
                if max_links[k] < cont: max_links[k] = cont
    score = max_links[0] ** 2 + max_links[1] ** 2 + max_links[2] ** 2 
    return score

def put_candy(f, kind, box):
    # fを座標に変換
    i,j = convert_ft_to_Coordinate(f,box)
    box[i][j][kind] = 1
    return box

l = list(map(int, input().split()))
dirs = ['F', 'R', 'B', 'L']

box = [[[0,0,0] for i in range(N)] for j in range(N)]

for t in range(100):
    kind = l[t]-1
    f = int(input())

    box = put_candy(f, kind, box)
    new_score = []


    for dir in dirs:
        box_new = copy.copy(tilt_box(dir, copy.copy(box)))
        new_score.append(calc_score(box_new))
    max_dir = new_score.index(max(new_score))
    print(dirs[max_dir])



    box = tilt_box(max_dir, box)

