class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        curr = self.head
        new_node = Node(value)
        # [] [] [] [] [] [] --> new_node
        #               curr --> new_node
        while curr.next is not None:
            curr = curr.next

        curr.next = new_node

    def get_nth_node(self, index):
        curr = self.head
        # []  [] [] [] []  []
        #           x
        count = 0

        while count < index:
            curr = curr.next

        return curr

    def insert(self, index, value):
        new_node = Node(value)

        #  [1] -> [prev]
        #  new_node -> -> [2] [3] [4]
        if index == 0:
            new_node.next = self.head
            self.head = new_node

        else:
            prev_node = self.get_nth_node(index - 1)
            old_next = prev_node.next
            prev_node.next = new_node
            new_node.next = old_next

    def print_all(self):

        curr = self.head

        while curr is not None:
            print(curr.value)
            curr = curr.next


def reverse_linked_list(head):
    curr = head
    next = None
    prev = None

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    head = curr
    return head