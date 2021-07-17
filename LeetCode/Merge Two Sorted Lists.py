# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1) # 결과 리스트 초기화
        cursor = head
        
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                cursor.next = l1
                l1 = l1.next # 다음 노드로 업데이트
            else:
                cursor.next = l2
                l2 = l2.next
                
            cursor = cursor.next # 포인터를 다음 노드로 옮기기
        
        # while문 종료 조건 -> l1이 None이 되었거나 l2가 None이 됨
        if l1 != None: # l2가 None일 경우
            cursor.next = l1
        else: # l1이 None일 경우
            cursor.next = l2
           
        # l1과 l2가 모두 빈 linked list일 경우 head.next는 빈 리스트가 됨
        return head.next
