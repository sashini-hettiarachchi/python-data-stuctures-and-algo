class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def traverse(self):
        if self.head is None:
            print("Linked list is Empty")
        else:
            node = self.head
            while node is not None:
                print(node.value, end=" ")
                node = node.next

    # def insert(self, value, location):
    #     newNode = Node(value)
    #     if self.head is None:
    #         self.head = newNode
    #         self.tail = newNode
    #     else:
    #         if location == 0:
    #             newNode.next = self.head
    #             self.head = newNode


node1 = Node(5)
node2 = Node(100)
node3 = Node(83)
node1.next = node2
node2.next = node3

singleLinkedList = SinglyLinkedList()
singleLinkedList.head = node1
singleLinkedList.tail = node3

singleLinkedList.traverse()

# for node in singleLinkedList:
#     print(node.value)

