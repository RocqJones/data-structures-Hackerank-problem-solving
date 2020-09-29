class SinglyLinkedListNode:

    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

def print_singly_linked_list(node):
    while node:
        print(node.data)
        node = node.next

# Complete the insertNodeAtHead function below.
def insertNodeAtHead(llist, data):
    new_node = SinglyLinkedListNode(data)

    if not llist:
        llist = new_node
    else:
        new_node.next = llist
        llist = new_node

    return new_node

if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head
    
    print_singly_linked_list(llist.head)

"""
SAMPLE INPUT
5
383
484
392
975
321

OUTPUT
321
975
392
484
383
"""