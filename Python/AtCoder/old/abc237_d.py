class Node:
    def __init__(self, val):
        self.val = val
        self.le = None
        self.ri = None

def main():
    A = [0]
    n = int(input())
    node_list = []
    bef_node = Node(0)
    node_list.append(bef_node)
    S = input()
    for i, c in enumerate(S, 1):
        cur_node = Node(i)
        node_list.append(cur_node)
        if c == 'L':
            # bef_nodeの左にcur_nodeを挿入
            pre_le_node = bef_node.le
            bef_node.le = cur_node
            cur_node.ri = bef_node
            cur_node.le = pre_le_node
            if pre_le_node:
                pre_le_node.ri = cur_node
        else:
            pre_ri_node = bef_node.ri
            bef_node.ri = cur_node
            cur_node.le = bef_node
            cur_node.ri = pre_ri_node
            if pre_ri_node:
                pre_ri_node.le = cur_node
        bef_node = cur_node

    # search_smallest_node
    cur_node = node_list[0]
    while True:
        if cur_node.le:
            cur_node = cur_node.le
        else:
            break

    ans_list = []
    while True:
        ans_list.append(cur_node.val)
        cur_node = cur_node.ri
        if cur_node is None:
            break

    print(*ans_list)


main()
