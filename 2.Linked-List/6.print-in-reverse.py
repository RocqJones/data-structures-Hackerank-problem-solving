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
        print(node.data, end='')

        node = node.next

# Complete the reversePrint function below.
def reversePrint(head):
    if head:
        stack = [head]
        while stack[-1].next:
            node = stack[-1]
            stack.append(node.next)

        while stack:
            node = stack.pop()
            print(node.data)

if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        reversePrint(llist.head)

"""
SAMPLE INPUT
3
5
16
12
4
2
5
3
7
3
9
5
5
1
18
3
13

OUTPUT
5
2
4
12
16
9
3
7
13
3
18
1
5
"""