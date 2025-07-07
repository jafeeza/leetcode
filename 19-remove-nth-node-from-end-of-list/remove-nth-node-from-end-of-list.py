# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        length=0
        first=head
        while first is not None:
            length+=1
            first=first.next
        length-=n
        prev=dummy
        while length>0:
            length-=1
            prev=prev.next
        prev.next=prev.next.next
        return dummy.next
