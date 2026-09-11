# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1: 
            return list2
        if not list2: 
            return list1 
        
        dumy = ListNode()
        prev = dumy
        cur1 = list1
        cur2 = list2 

        while cur1 and cur2: 
            if cur1.val <= cur2.val: 
                prev.next = cur1
                prev = cur1
                cur1 = cur1.next
            else: 
                prev.next = cur2
                prev = cur2
                cur2 = cur2.next
        
        prev.next = cur1 or cur2 

        return dumy.next
