
from arrays import Array


class ArrayStack(object):
    """ Array-based stack implementation."""

    DEFAULT_CAPACITY = 10  # Class variable for all array stacks

    def __init__(self):
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)
        self._top = -1
        self._size = 0

    def push(self, newItem):
        """Inserts newItem at top of stack."""
        if self._size == len(self._items):  # resize if necessary
            new_array = Array(self._size * 2)
            for i in range(len(self._items)):
                new_array[i] = self._items[i]
            self._items = new_array

        self._top += 1  # push a new item
        self._size += 1
        self._items[self._top] = newItem

    def pop(self):
        """Removes and returns the item at top of the stack.
        Precondition: the stack is not empty."""
        if self._size == 0:  # add constraint
            raise ValueError
        else:
            oldItem = self._items[self._top]
            self._items[self._top] = None
            self._top -= 1
            self._size -= 1
            return oldItem

    def peek(self):
        """Returns the item at top of the stack.
        Precondition: the stack is not empty."""
        if self._size == 0:  # add constraint
            raise ValueError
        else:
            return self._items[self._top]

    def isEmpty(self):
        """Check if the stack is empty"""
        return self._size == 0

    def __len__(self):
        """Returns the number of items in the stack."""
        return self._size

    def __str__(self):
        result = ''
        for i in range(self._size):
            result += str(self._items[i]) + ' '
        return result


def main():

    s = ArrayStack()
    print("Length:", len(s))
    print("Empty:", s.isEmpty())
    print("Push 1-10")

    for i in range(10):
        s.push(i + 1)
    print("Peeking:", s.peek())
    print("Items (bottom to top):", s)
    print("Length:", len(s))
    print("Empty:", s.isEmpty())
    print("Push 11")
    s.push(11)
    print("Popping items (top to bottom):",)
    while not s.isEmpty():
        print(s.pop(),)
        print("\nLength:", len(s))
    print("Empty:", s.isEmpty())


if __name__ == '__main__':
    main()
