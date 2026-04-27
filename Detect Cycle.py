class ListNode:
    def __init__(self, val):
        self.val, self.next = val, None

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next           # 1 step
        fast = fast.next.next      # 2 steps
        if slow == fast:
            return True       # Floyd's meeting point
    return False

# Build: 1 → 2 → 3 → 4 → (back to 2)
n1,n2,n3,n4 = [ListNode(i) for i in [1,2,3,4]]
n1.next=n2; n2.next=n3; n3.next=n4; n4.next=n2
print(has_cycle(n1))  # True
