class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedListNode:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, data):
        # call from object class Node
        node = Node(data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def printLinkedList(head):
    temp = head
    while temp is not None:
        print(temp.data)
        temp = temp.next

if __name__ == '__main__':
    input_count = int(input())

    input_data = list(map(int, input().rstrip().split()))

    # object of class
    new_node = SinglyLinkedListNode()

    # insert actual data in node: this replaces the 'temp/temporary data' in the class
    new_node.insert_node(input_data)

    printLinkedList(new_node.head)

"""
- The rstrip() method removes any trailing characters (characters at the end a string)
- The split() method splits a string into a list

INPUT SAMPLE DATA
3
16 13 452
OUTPUT
[16, 13, 452]
"""