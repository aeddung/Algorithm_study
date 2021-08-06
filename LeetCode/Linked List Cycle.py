# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # base case
        if not head:
            return False
        if not head.next:
            return False
        
        first = head # 앞서가는 노드
        second = head # 뒤 따르는 노드
        while first != None and first.next != None:
            first = first.next.next
            second = second.next
            if first == second:
                return True
        return False
