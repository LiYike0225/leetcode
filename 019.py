class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def getLength(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        dummy = ListNode(0, head) #val = 0，指针指向head
        length = getLength(head)
        cur = dummy
        for i in range(0, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next

        return dummy.next

