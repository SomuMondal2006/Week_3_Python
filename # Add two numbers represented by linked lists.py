# Add two numbers represented by linked lists
# https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1



# Definition for singly-linked list.
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

# Function to reverse a linked list
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# Function to add two linked lists
def addTwoLists(first, second):
    # Reverse both lists so that we can add from least significant digit
    first = reverse_list(first)
    second = reverse_list(second)

    carry = 0
    result_head = None
    result_tail = None

    while first or second or carry:
        val1 = first.data if first else 0
        val2 = second.data if second else 0

        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        new_node = Node(digit)
        if not result_head:
            result_head = new_node
            result_tail = new_node
        else:
            result_tail.next = new_node
            result_tail = result_tail.next

        if first:
            first = first.next
        if second:
            second = second.next

    # Reverse the result to get the final sum in correct order
    result_head = reverse_list(result_head)

    # Remove leading zeros
    while result_head and result_head.data == 0 and result_head.next:
        result_head = result_head.next

    return result_head

# Helper function to print linked list
def print_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

# Example usage:
# List 1: 4 -> 5  (45)
head1 = Node(4, Node(5))
# List 2: 3 -> 4 -> 5  (345)
head2 = Node(3, Node(4, Node(5)))

result = addTwoLists(head1, head2)  # Expected: 3 -> 9 -> 0 (390)
print_list(result)

# List 1: 0 -> 0 -> 6 -> 3 (63)
head3 = Node(0, Node(0, Node(6, Node(3))))
# List 2: 0 -> 7 (7)
head4 = Node(0, Node(7))

result = addTwoLists(head3, head4)  # Expected: 7 -> 0 (70)
print_list(result)
