# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head

        def solve(head: Optional[ListNode]):
            nonlocal curr
            if not head:
                return

            solve(head.next)
            if curr.next == None:
                return
            if curr == head:
                curr.next = None
                return
            temp = curr.next
            curr.next = head
            head.next = None if temp == head else temp
            curr = temp

        solve(head)
