class SinglyLinkedListNode:

    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node):
    while node:
        print(str(node.data))

        node = node.next

# Complete the reverse function below.
# For your reference:
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
def reverse(head):
    new_head = None

    while head:
        temp = head
        head = temp.next
        temp.next = new_head
        new_head = temp

    return new_head

if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1)

"""
SAMPLE INPUT
1
5
1
2
3
4
5

SAMPLE OUTPUT
5 4 3 2 1
"""