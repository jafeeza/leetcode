# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr=head
        l=[]
        while curr:
            l.append(curr.val)
            curr=curr.next
        if len(l)<=1:
            return True
        first=0
        last=len(l)-1
        while first<last:
            if l[first]!=l[last]:
                return False
            first+=1
            last-=1
        return True
        