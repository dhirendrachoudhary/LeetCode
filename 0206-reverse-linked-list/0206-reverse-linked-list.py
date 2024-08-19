# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            # store curr add in a temp
            tmp = curr.next
            
            # change curr.next to the prev
            curr.next = prev
            
            # change the prev to curr
            prev = curr
            
            # update curr with temp
            curr = tmp
        return prev
        
            