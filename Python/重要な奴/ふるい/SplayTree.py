class SplayTree:
    class Node:
        def __init__(self):
            self.left = None
            self.right = None
            self.parent = None
            self.size = 1
            self.value = None
            # self.minimu = 0  # 必要に応じて実装

        def rotate(self):
            """自分を上に持ち上げる回転
            self.parentとselfを入れ替える回転を実装する
            張り替える編は6つ
            parentとparent.parentをつなぐ辺
            selfとparentをつなぐ辺
            self.left/rightとselfをつなぐ辺
            """
            parent = self.parent  # 必ずある
            grand_parent = self.parent.parent  # Noneかも
            # selfがparentの左にあるか右にあるかで変わる
            if parent.left == self:
                child = self.right  # Noneかも
            else:
                child = self.left  # Noneかも
            # 辺の張替え1~2,self.left/rightがかかわるやつ
            if parent.left == self:
                self.right = parent
                parent.left = child
            else:
                self.left = parent
                parent.right = child
            # 辺の張替え3,grand_parent.left/rightがかかわるやつ
            if grand_parent is not None:
                if (grand_parent.left == parent):
                    grand_parent.left = self
                elif (grand_parent.right == parent):
                    grand_parent.right = self
            # 4つめ～6つめの辺
            self.parent = grand_parent
            parent.parent = self
            if child is not None:
                child.parent = parent
            parent.update()
            self.update()

        def splay(self):
            """このNodeを回転させて一番上に持ってくる
            grand_parentがいない場合は、回転一回でよい
            grand_parentがいて、関係が同じ(grand_parent.left.left == self)場合は
                parent->selfの順で回転
            関係が違ったら、selfを二回回転
            """
            if self.state() == 'no_parent':
                return

            while self.parent.state() != 'no_parent':
                if self.state():
                    self.rotate()
                elif self.state() == self.parent.state():
                    self.parent.rotate()
                    self.rotate()
                else:
                    self.rotate()
                    self.rotate()

        def state(self):
            """親から見て自分がleftかrightか
            親がいない場合はno_parent
            Returns:
                [type]: [description]
            """
            if self.parent is None:
                return 'no_parent'
            if self.parent.left == self:
                return 'left'
            else:
                return 'right'

        def update(self):
            """頂点の部分木のサイズを張り替えたりする
            サイズは、左右のノードのサイズに1(自分自身)を足したもの
            """
            size = 1
            # minimum = 0
            if self.left is not None:
                size += self.left.size
                # self.minimum = min(self.left.minimun, self.minimum)
            if self.right is not None:
                size += self.right.size
                # self.minimum = min(self.right.minimun, self.minimum)
            self.size = size
            # self.minimum = minimum

        def in_order(self):
            """間順操作（DFS)して、イテレータに用いる

            Returns:
                [type]: [description]
            """
            if self.left:
                for n in self.left.in_order():
                    yield n

            yield self

            if self.right:
                for n in self.right.in_order():
                    yield n

    def __init__(self, init_list=[]):
        """空のSplayTreeを与える
        引数にlistを入れた場合、listからなるSplayTreeを与える
        Args:
            init_list (list, optional): [description]. Defaults to [].
        """
        self.root = None
        if len(init_list) > 0:
            sorted_list = sorted(init_list)
            child = None
            for i in sorted_list:
                me = self.Node()
                me.value = i
                me.left = child
                if child is not None:
                    child.parent = me
                me.update()
                child = me
            self.root = me

    def get(self, ind: int, root=None):
        """左からind番目のNodeを得る
        第二引数のrootに値を入れると、root以下の部分木に対して処理する
        Args:
            ind ([type]): [description]
        """
        if root is None:
            root = self.root
        now_node = root
        while True:
            if now_node.left is None:
                left_size = 0
            else:
                left_size = now_node.left.size
            if ind < left_size:
                now_node = now_node.left
            if ind == left_size:
                now_node.splay()
                self.root = now_node
                return now_node
            if ind > left_size:
                now_node = now_node.right
                ind = ind - left_size - 1

    def merge(self, left: Node, right: Node):
        """leftのNodeとrightのNodeをつなげ
        leftとrightからなる木を作成する
        """
        if left is None:
            return right
        if right is None:
            return left
        left_root = self.get(left.size-1, left)
        left_root.right = right
        left_root.update()
        return left_root

    def split(self, ind: int, root=None):
        """indで左右に木を分割し、分けた二つの部分木(Node)を返す

        Args:
            ind ([type]): [description]
        """
        if root is not None:
            root = self.root
        if ind == 0:
            return [None, root]
        if ind == root.size:
            return [root, None]
        root = self.get(ind, root)
        left_root = root.left
        right_root = root
        right_root.left = None
        left_root.parent = None
        right_root.update()
        return [left_root, right_root]

    def insert_node(self, ind: int, node: Node, root=None):
        """
        指定したnodeを指定したindに挿入する

        Args:
            ind (int): [description]
            node (Node): [description]
            root ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        if root is not None:
            root = self.root
        trees = self.split(self, ind, root)
        left_root = trees[0]
        right_root = trees[1]
        return self.merge(self.merge(left_root, node), right_root)

    def delete(self, ind: int, root=None):
        if root is not None:
            root = self.root
        root = self.get(ind, root)
        left_root = root.left
        right_root = root.right
        if left_root is not None:
            left_root.parent = None
        if right_root is not None:
            right_root.parent = None
        root.left = None
        root.right = None
        root.update()

        return [self.merge(left_root, right_root), root]

    def __iter__(self):
        """イテレータを設定
        """
        if self.root:
            return self.root.in_order()


li = list([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
sp = SplayTree(li)
print(sp.get(5).value)
#sp.delete(3)
for i in range(5, 9):
    print(sp.get(i).value)
for i in sp:
    print(i.value)
