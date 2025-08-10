# Insert in middle of linked list
# https://www.geeksforgeeks.org/problems/insert-in-middle-of-linked-list/1



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_in_middle(head, x):
    new_node = Node(x)
    
    if head is None:
        return new_node

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    new_node.next = slow.next
    slow.next = new_node

    return head

def build_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end="->" if current.next else "\n")
        current = current.next

input_values = list(map(int, input("Enter linked list values (space separated): ").split()))
x = int(input("Enter the value to insert in the middle: "))

head = build_linked_list(input_values)
head = insert_in_middle(head, x)

print("Modified Linked List:")
print_linked_list(head)
