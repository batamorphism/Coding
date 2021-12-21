a = [list(map(int, input().split())) for _ in range(4)]

dxdy = [(-1,0), (1,0), (0,-1), (0,1)]

ans = 0
for mask in range(1<<16):
    nodes = set()
    not_nodes = set()
    flag = True
    for i in range(4):
        for j in range(4):
            if mask>>(4*i+j) & 1:
                nodes.add((i,j))
            else:
                not_nodes.add((i,j))
                if a[i][j]:
                    flag = False
    if flag:
        # DFS
        todo = [nodes.pop()]
        while todo:
            x, y = todo.pop()
            for dx, dy in dxdy:
                if (x+dx,y+dy) in nodes:
                    nodes.remove((x+dx,y+dy))
                    todo.append((x+dx,y+dy))
        if nodes:
            continue

        for i in range(6):
            not_nodes.add((-1,i))
            not_nodes.add((i,4))
            not_nodes.add((4,i))
            not_nodes.add((i,-1))

        # DFS
        todo = [not_nodes.pop()]
        while todo:
            x, y = todo.pop()
            for dx, dy in dxdy:
                if (x+dx,y+dy) in not_nodes:
                    not_nodes.remove((x+dx,y+dy))
                    todo.append((x+dx,y+dy))
        if not_nodes:
            continue

        ans += 1

print(ans)