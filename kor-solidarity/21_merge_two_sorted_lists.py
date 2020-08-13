# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        sorted_list = []
        obj1 = l1
        obj2 = l2
        while obj1:
            if obj1.val is not None:
                sorted_list.append(obj1.val)
            obj1 = obj1.next

        while obj2:
            if obj2.val is not None:
                sorted_list.append(obj2.val)
            obj2 = obj2.next
        sorted_list.sort()

        node = None
        for i in range(len(sorted_list)-1, -1, -1):
            print(i)
            node = ListNode(sorted_list[i], node)

        return node


        print(l1.val, l1.next)


l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

# Solution().mergeTwoLists(l1, l2)
Solution().mergeTwoLists(ListNode(None), ListNode(0))
