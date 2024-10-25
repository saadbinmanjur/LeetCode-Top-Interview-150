# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        numbers_range = [0] * 201

        temp = head

        while temp:
            num = temp.val
            offset_val = num + 100
            numbers_range[offset_val] += 1
            temp = temp.next
        
        new_head = None
        temp = None

        for i in range(len(numbers_range)):
            freq = numbers_range[i]
            if freq > 1:
                continue
            elif freq == 1:
                if temp:
                    tail_node = ListNode(i-100)
                    temp.next = tail_node
                    temp = temp.next
                else:
                    new_head = ListNode(i-100)
                    temp = new_head
        
        return new_head