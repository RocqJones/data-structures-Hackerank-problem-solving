import math

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node):
    while node:
        print(node.data)
        node = node.next

# Complete the insertNodeAtTail function below.
def insertNodeAtTail(head, data):
    if (head == None):
        head = SinglyLinkedListNode(data)
    else:
        current = head
        while (current.next != None):
            current = current.next
        current.next = SinglyLinkedListNode(data)
    return head

if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head)

"""
SAMPLE INPUT
5
141
302
164
530
474

OUTPUT
141
302
164
530
474
"""