''':arg
Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

list1 = [1, 2, 4]
list2 = [1, 3, 4]


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        result = []
        result.extend(l1)
        result.extend(l2)

        return sorted(result)

s = Solution()
print(s.mergeTwoLists(list1, list2))
