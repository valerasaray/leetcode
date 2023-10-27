'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#тестовые списки
l13 = ListNode(1, None)
l12 = ListNode(1, l13)
l11 = ListNode(0, l12)

l23 = ListNode(1, None)
l22 = ListNode(1, l23)
l21 = ListNode(1, l22)

class Solution:
    def listToNumber(self, l: Optional[ListNode]):
        result = ''
        while l != None:
            result += str(l.val)
            l = l.next
        return int(result[::-1])
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = None
        for i in str(self.listToNumber(l1) + self.listToNumber(l2)):
            l3 = ListNode(int(i), l3)
        return l3

#вывод начального элемента итогового списка
s = Solution()
print(s.addTwoNumbers(l11, l21).val)

