class train:
    def __init__(self, val):
        self.val = val
        self.le = None
        self.ri = None
        self.head = self

    def join(self, other):
        self.ri = other
        other.le = self
        other.head = self

    def disconnect(self):
        self.ri.head = self.ri
        self.ri.le = None
        self.ri = None


def main():
    n, q_end = map(int, input().split())
    train_list = [train(i) for i in range(n)]
    query_list = [map(int, input().split()) for _ in range(q_end)]
    for query in query_list:
        q, *xy = query
        if q == 3:
            x = xy[0]-1
        else:
            x = xy[0]-1
            y = xy[1]-1
        if q == 1:
            train_list[x].join(train_list[y])
        elif q == 2:
            train_list[x].disconnect()
        else:
            head = train_list[x].head
            while head != head.head:
                head = head.head
            t = head
            ans = []
            while t is not None:
                ans.append(t.val+1)
                t = t.ri
            print(len(ans), *ans)


main()
