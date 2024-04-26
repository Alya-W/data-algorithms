import numpy as np
from node import Node


def length(head):
    """Returns the number of items in the linked structure
    referred to by head."""
    length = 0
    probe = head
    while probe is not None:
        length += 1
        probe = probe.next
    return length


def remove(index, head):
    """Removes the item at index from the linked structure
        referred to by head and returns the tuple (head, item)
        Precondition: 0 <= index < length(head)"""
    if 0 <= index < length(head):
        if index == 0 or head.next is None:
            removedItem = head.data
            head = head.next
            return head, removedItem
        else:
            probe = head
            while index > 1 and probe.next.next is not None:
                probe = probe.next
                index -= 1
            removedItem = probe.next.data
            probe.next = probe.next.next
            return head, removedItem
    else:
        raise ValueError


def insert(index, newItem, head):
    if head is None or index <= 0:
        head = Node(newItem, head)
        return head
    else:
        probe = head
        while index > 1 and probe.next is not None:
            probe = probe.next
            index -= 1
        probe.next = Node(newItem, probe.next)


def printStructure(head):
    """Prints the items in the structure referred to by head."""
    probe = head
    while probe is not None:
        print(probe.data, )
        probe = probe.next


def main():
    """Tests modifications."""
    head = None
    print('-----------------------')
    head = insert(0, "1", head)
    print("1:", )
    printStructure(head)
    print('-----------------------')

    (head, item) = remove(0, head)
    print("1:", item)
    printStructure(head)
    print('-----------------------')

    # Add five nodes to the beginning of the linked structure
    for count in range(1, 6):
        head = Node(count, head)

    (head, item) = remove(0, head)
    print("5 4 3 2 1:", item, '\n')
    printStructure(head)
    print('-----------------------')

    (head, item) = remove(length(head) - 1, head)
    print("1 4 3 2:", item, '\n')
    printStructure(head)
    print('-----------------------')

    (head, item) = remove(1, head)
    print("3 4 2:", item, '\n')
    printStructure(head)
    print('-----------------------')

    #remove(4, head)

    """
    s = ArrayStack()
    for i in range(4):
        s.push(2*i)
        s.push(3*i)
    for i in range(4):
        s.push(s.pop()-s.pop())
    for i in range(4):
        print(s.pop())
    
    OUTPUT: 
    -10
    2
    0
    0
    """


if __name__ == "__main__":
    main()


def replace(head, target, newItem):
    probe = head
    while probe is not None and target != probe.data:
        probe = probe.next
    if probe is not None:
        probe.data = newItem
        return True
    else:
        return False


def initialize(depth, row, column):
    new_array = np.zeros((depth, row, column))
    for k in range(new_array.shape[0]):
        for j in range(new_array.shape[1]):
            for m in range(new_array.shape[2]):
                new_array[k][j][m] = k + j + m
    return new_array


