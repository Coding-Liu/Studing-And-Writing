# 前序遍历
def pre_order(btree):
    if btree:
        print(btree.data)
        pre_order(btree.lchild)
        pre_order(btree.rchild)


# 中序遍历
def in_order(btree):
    if btree:
        in_order(btree.lchild)
        print(btree.data)
        in_order(btree.rchild)


# 后续遍历
def post_order(btree):
    if btree:
        post_order(btree.lchild)
        post_order(btree.rchild)
        print(btree.data)


# 层次遍历
class Queue:
    # 定义一个循环队列
    def __init__(self, capacity=10):
        self.front = 0
        self.rear = 0
        self.data = [None] * capacity
        self.size = 0
        self.maxsize = capacity

    def en_queue(self, node):
        self.rear = (self.rear + 1) % self.maxsize
        self.data[self.rear] = node
        self.size += 1

    def de_queue(self):
        self.front = (self.front + 1) % self.maxsize
        self.size -= 1
        return self.data[self.front]


def level_order(bt):
    queue = Queue()
    queue.en_queue(bt)
    while queue.size != 0:
        q = queue.de_queue()
        print(q.data, end=" ")
        if q.lchild:
            queue.en_queue(q.lchild)
        if q.rchild:
            queue.en_queue(q.rchild)
