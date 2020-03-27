#  前驱结点


def find_parent(bstree, value):
    """
    查找二叉排序树中值为value的前驱结点
    :param bstree: 根节点
    :param value: 值
    """
    p = bstree
    pre = None
    while p:
        if value < p.data:
            pre = p
            p = p.lchild
        elif value > p.data:
            pre = p
            p = p.rchild
        else:
            break
    if p is None:
        raise Exception("Not Exist")
    else:
        return pre.data


# 后继节点

def find_post(bstree, value):
    p = bstree
    while p:
        if value < p.data:
            p = p.lchild
        elif value > p.data:
            p = p.rchild
        else:
            break
    if p is None:
        raise Exception("Not Exist")
    else:
        if p.lchild:
            re = p.lchild
        else:
            re = p.rchild
        return re
