class linkedList:
	def __init__(self, data, pnext=None):
        self.data = data
        self.next = pnext
        

# 打印链表
def show(node):
    p = node
    while p:
        print(p.data, end=' ')
        p = p.next
    print('\n')
    
#创建一个单链表
def createLinkenlist(lst=[]):
    linkedlst = linkedList(lst[0])
    head = linkedlst
    p = head
    for _ in lst[1:]:
        node = linkedList(_)
        p.next = node
        p = node
    return head
    
# 在链表index处的结点后插入值为value的结点
def insert(index, head, value):
    count = 0
    p = head
    
    while p != None:
        if count == index:
            break
        else:
            p = p.next
            count += 1
    node = linkedList(value)
    node.next = p.next
    p.next = node
    
# 删除链表中的所有值为value的结点
def delete(head, value):
    while head.data == value:
        head = head.next
    
    pre = head
    q = pre.next
    while q != None:
        if q.data == value:
            pre.next = q.next
            q = q.next
        else:
            pre = q
            q = q.next
    return head