class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None



# 思路一：借助两个结点直接实现链表的反转
class Solution:
    def reverse_list(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
        
# 思路二：使用递归实现
class Solution:
    def reverse_list(self, head):
        if not head:
            return []
        return self.reverse_list(head.next) + [head.val]
        
        
# 思路三：使用栈实现，将链表放入栈，然后出栈
class Solution:
    def reverse_list(self, head):
        res = []
        while head:
            head = head.next
            res.append(head.val)
        return res[::-1]
        
