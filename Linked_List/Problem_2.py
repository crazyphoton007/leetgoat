

#  Merge two sorted list

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]


## For this time exceeds but understand how pointer moves

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummmy = ListNode()
        insertNext = dummy

        greenArrow = list1
        redArrow = list2

        while greenArrow and redArrow:
            greenValue = greenArrow.val
            redValue = redArrow.val

            if greenValue <= redValue:
               insertNext.next = greenArrow
               greenArrow = greenArrow.next

            else:
                insertNext.next = redArrow
                redArrrow = redArrow.next
            
            insertNext = insertNext.next

        return dummy.next



