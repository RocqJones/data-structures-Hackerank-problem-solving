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
        print(node.data)

        node = node.next

# Complete the deleteNode function below.
def deleteNode(head, position):
    if head:
        if position == 0:
            head = head.next

        else:
            previous = None
            current = head
            current_position = 0
            while (current_position < position) and (current.next is not None):
                previous = current
                current = current.next
                current_position += 1

            previous.next = current.next

    return head

if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    llist1 = deleteNode(llist.head, position)

    print_singly_linked_list(llist1)

"""
Explanation
The original list is 20 -> 6 -> 2 -> 19 -> 7 -> 4 -> 15 -> 9. After deleting the node at position 3, 
the list will be 20 -> 6 -> 2 -> 7 -> 4 -> 15 -> 9

SAMPLE INPUT
8
20
6
2
19
7
4
15
9
3

OUTPUT
20 6 2 7 4 15 9
"""