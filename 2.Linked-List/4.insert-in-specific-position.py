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

# Complete the insertNodeAtPosition function below.
def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)
    
    if position == 0:
        new_node.next = head
        return new_node

    previous_node = head
    while previous_node is not None:
        for _ in range(position-1):
            previous_node = previous_node.next

        new_node.next = previous_node.next
        previous_node.next = new_node

        return head

if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head)

"""
SAMPLE INPUT
3
16
13
7
1
2

Explanation
The initial linked list is '16 -> 13 -> 7'. Insert '1' at the position '2' which currently has '7' in it. 
The updated linked list is '16 -> 13 -> 1 -> 7'.

OUTPUT
16 13 1 7
"""