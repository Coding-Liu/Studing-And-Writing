class Node:
    def __init__(self, value, lchild=None, rchild=None):
        self.data = value
        self.lchild = lchild
        self.rchild = rchild


class BSTree:
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value):
        """
        插入值为value的结点
        二叉排序树插入的结点一定为叶子结点
        """
        node = Node(value)
        p = self.root
        pre = p
        while p:
            if p.data > value:
                p = p.lchild
            elif p.data < value:
                p = p.rchild
            else:
                break
        if p is None:
            if pre.data < value:
                pre.lchild = node
            else:
                pre.rchild = node

    def find(self, value):
        p = self.root
        while p:
            if p.data > value:
                p = p.rchild
            elif p.data < value:
                p = p.rchild
            else:
                print("已找到该节点")
        if p is None:
            raise Exception("Not Exist")
        return p

    def find_parent(self, target):
        """查找二叉排序树中目标节点的父节点"""
        p = self.root
        pre = None
        while p:
            if target.data < p.data:
                pre = p
                p = p.lchild
            elif target.data > p.data:
                pre = p
                p = p.rchild
            else:
                if p is target:
                    break
                else:
                    pre = p
                    p = p.rchild
        if p is None:
            raise Exception("Not Exist")
        else:
            return pre

    def remove(self, node, value):
        '''
        删除二叉排序树中值为value的结点
        目标结点p的位置可能有以下三种情况：
        1) p为叶子结点：直接删除即可
        2) p有左子树或右子树其中之一：删除p，p的父结点连接到p的子树
        3) p同时有左右子树：选中序序列中与p相邻的两个结点之一覆盖p结点，
        再依据1)或2)删除该结点
        '''
        p = node
        pre = None
        while p:
            if p.data > value:
                pre = p
                p = p.lchild
            elif p.data < value:
                pre = p
                p = p.rchild
            else:  # 找到待删结点之后进行的操作
                if p.lchild and p.rchild:  # 情况3)要删除的结点
                    temp = p.rchild
                    while temp.lchild:
                        temp = temp.lchild
                    p.data = temp.data  # 找到中序序列后一个结点temp覆盖待删结点p

                    '''
                    以下在二叉排序树中找到temp结点并删除（由于此时有两个相同值的结点，
                    故在查找时还需用地址进行比较（findParent（target）中））
                    temp结点只有两种可能：
                    1)叶子结点
                    2)只有右子树
                    '''
                    if temp.lchild == None and temp.rchild == None:  # 情况1)待删结点为叶子结点
                        self._removeLeaf(temp)
                        break
                    else:  # 情况2)待删结点只有右子树
                        parentTemp = self.findParent(temp)
                        self._changeChild(parentTemp, temp, temp.rchild)
                elif p.lchild:  # 情况2)待删结点只有左子树
                    self._changeChild(pre, p, p.lchild)
                    break
                elif p.rchild:  # 情况2)待删结点只有右子树
                    self._changeChild(pre, p, p.rchild)
                    break
                else:  # 情况1)待删结点为叶子结点
                    self._removeLeaf(p)
                    break








