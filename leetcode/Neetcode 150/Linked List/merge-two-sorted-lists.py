class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into one sorted list.

        Parameters:
            list1 (ListNode): The head of the first sorted linked list.
            list2 (ListNode): The head of the second sorted linked list.

        Returns:
            ListNode: The head of the merged sorted linked list.
        """

        # Create a dummy node to serve as the head of the merged list.
        dummy = ListNode()
        # Initialize a tail variable to keep track of the current node where new nodes will be attached.
        tail = dummy

        # Iterate through both lists while they are not empty.
        while list1 and list2:
            # Compare the values of the current nodes from list1 and list2.
            if list1.val < list2.val:
                # Attach the current node from list1 to the tail.
                tail.next = list1
                # Move the list1 pointer to the next node in list1.
                list1 = list1.next
            else:
                # Attach the current node from list2 to the tail.
                tail.next = list2
                # Move the list2 pointer to the next node in list2.
                list2 = list2.next
            # Move the tail pointer to the newly attached node.
            tail = tail.next

        # Check if there are any remaining nodes in either list1 or list2.
        # Attach the rest of the nodes to the tail since they are already sorted.
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # Return the next node after the dummy node, which is the head of the merged sorted list.
        return dummy.next