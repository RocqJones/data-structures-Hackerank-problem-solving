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

# Complete the getNode function below.
# For your reference:
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
def getNode(head, positionFromTail):
    my_list = []
    while head:
        my_list.append(head.data)
        head = head.next

    # return t[-(positionFromTail + 1)]
    print(my_list[-(positionFromTail + 1)])

if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        position = int(input())

        getNode(llist.head, position)