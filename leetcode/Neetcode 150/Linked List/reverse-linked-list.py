# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list.

        Parameters:
            head (Optional[ListNode]): The head of the input singly linked list.

        Returns:
            Optional[ListNode]: The head of the reversed singly linked list.

        Approach:
            The algorithm uses three pointers: `prev`, `curr`, and `nxt`.
            `prev` starts as None, `curr` starts as the head of the original list.
            We traverse the original list while updating the `next` pointer of each node to point to its previous node.
            The `prev` pointer keeps track of the reversed list's head, and `curr` moves forward.
            Once we reach the end of the list (curr becomes None), we return the `prev` pointer.

        Complexity Analysis:
            - Time Complexity: O(n), where n is the number of nodes in the linked list.
            - Space Complexity: O(1), as we are using a constant amount of extra space.

        """
        prev, curr = None, head

        while curr:
            nxt = curr.next    # Store the next node in the original list.
            curr.next = prev   # Point the current node's next to the previous node, reversing the link.
            prev = curr        # Move `prev` to the current node (to be used as the next node's previous node).
            curr = nxt         # Move `curr` to the next node in the original list.

        return prev  # The `prev` pointer now points to the head of the reversed list.
