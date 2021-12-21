import sys
sys.setrecursionlimit(10**9)

class BinaryNode:
    def __init__(self, value=None):
        """BinaryNode
        順序付けられた値value
        value以下の値のNodeを持つleft
        valueより大きい値のNodeを持つright
        からなる
        Args:
            value ([type], optional): [description]. Defaults to None.
        """
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

    def compute_height(self):
        """BSTの設定の高さを計算する
        子の高さはadd時に常に計算
        """
        height = -1
        if self.left:
            height = max(height, self.left.height)
        if self.right:
            height = max(height, self.right.height)
        self.height = height

    def height_difference(self):
        """BSTのNodeの子の高さの差を計算する
        """
        left_target = 0
        right_target = 0
        if self.left:
            left_target = 1+self.left.height
        if self.right:
            right_target = 1+self.right.height
        return left_target-right_target

    def add_to_sub_tree(self, parent, val):
        """parentの部分木（あれば）にvalを追加し、回転によって変更された場合にrootを返す

        Args:
            parent ([type]): [description]
            val ([type]): [description]
        """
        if parent is None:
            return BinaryNode(val)
        parent = parent.add(val)
        return parent

    def add(self, val):
        """新たなNodeを追加する

        Args:
            val ([type]): 順序付けられた値
        """
        new_root = self
        if val <= self.value:
            # leftのnodeにvalを追加する
            self.left = self.add_to_sub_tree(self.left, val)
            if self.height_difference() == 2:
                if val <= self.left.value:
                    new_root = self.rotate_right()
                else:
                    new_root = self.rotate_left_right()
        else:
            # rightのnodeにvalを追加する
            self.right = self.add_to_sub_tree(self.right, val)
            if self.height_difference() == -2:
                if val > self.left.value:
                    new_root = self.rotate_left()
                else:
                    new_root = self.rotate_right_left()
        new_root.compute_height()
        return new_root

    def rotate_right(self):
        """このNodeで右回転する

        Returns:
            [BinaryNode]: 回転した後のNode
        """
        new_root = self.left
        grandson = new_root.right
        self.left = grandson
        new_root.right = self

        self.compute_height()
        return new_root

    def rotate_right_left(self):
        """このNodeで右回転してから左回転する

        Returns:
            [BinaryNode]: 回転した後のNode
        """
        child = self.right
        new_root = child.left
        grand1 = new_root.left
        grand2 = new_root.right
        child.left = grand2
        child.right = grand1
        new_root.left = self
        new_root.right = child
        child.compute_height()
        self.compute_height()
        return new_root

    def rotate_left(self):
        """このNodeで左回転する

        Returns:
            [BinaryNode]: 回転した後のNode
        """
        new_root = self.left
        grandson = new_root.left
        self.left = grandson
        new_root.left = self

        self.compute_height()
        return new_root

    def rotate_left_right(self):
        """このNodeで左回転してから右回転する

        Returns:
            [BinaryNode]: 回転した後のNode
        """
        child = self.left
        new_root = child.right
        grand1 = new_root.right
        grand2 = new_root.left
        child.right = grand2
        child.left = grand1
        new_root.right = self
        new_root.left = child
        child.compute_height()
        self.compute_height()
        return new_root

    def in_order(self):
        """間順操作（DFS)して、イテレータに用いる

        Returns:
            [type]: [description]
        """
        if self.left:
            for n in self.left.in_order():
                yield n

        yield self.value

        if self.right:
            for n in self.right.in_order():
                yield n


class BinaryTree:
    def __init__(self):
        """空の平衡二分探索木AVLを作成する
        """
        self.root = None

    def add(self, value):
        """valueを平衡二分探索木に追加する

        Args:
            value ([type]): [description]
        """
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)

    def __contains__(self, target):
        """targetがBSTに含まれることを確認する
        in演算子で使用可能

        Args:
            target ([type]): [description]
        """
        node = self.root
        while node:
            if target < node.value:
                node = node.left
            elif target > node.value:
                node = node.right
            else:
                return True
        return False

    def __iter__(self):
        """イテレータを設定
        """
        if self.root:
            return self.root.in_order()

    def search_lower(self, target):
        node = self.root
        lower_node = None
        while node:
            if target < node.value:
                node = node.left
            elif target > node.value:
                lower_node = node
                node = node.right
            else:
                lower_node = node
                return node
        return lower_node.value

    def search_higher(self, target):
        node = self.root
        higher_node = None
        while node:
            if target < node.value:
                higher_node = node
                node = node.left
            elif target > node.value:
                node = node.right
            else:
                higher_node = node
                return node
        return higher_node.value

    def search_high_low(self, target):
        node = self.root
        higher_node = None
        lower_node = None
        while node:
            if target < node.value:
                higher_node = node
                node = node.left
            elif target > node.value:
                lower_node = node
                node = node.right
            else:
                higher_node = node
                lower_node = node
                return node
        return [higher_node.value, lower_node.value]


def main():
    L, Q = map(int, input().split())

    C = []
    X = []

    bt = BinaryTree()

    for _ in range(Q):
        c, x = map(int, input().split())
        C.append(c)
        X.append(x)

    bt.add(0)
    bt.add(L)

    for (c, x) in zip(C, X):
        if c == 1:
            bt.add(x)
        else:
            ans_h, ans_l = bt.search_high_low(x)
            print(ans_h-ans_l)


main()
