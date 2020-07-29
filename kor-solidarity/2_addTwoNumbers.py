# Definition for singly-linked list.
# this is wrong.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ''
        num2 = ''
        for i in l1:
           num1 = str(i) + num1
        for i in l2:
           num2 = str(i) + num2
        result = str(int(num1) + int(num2))
        answer = []
        for i, j in enumerate(result):
            answer.insert(0, j)
        return answer





a = Solution()
print(a.addTwoNumbers([2, 4, 3], [5, 6, 4]))


