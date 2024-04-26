"""
File: arrays.py
Project 13.4
Name: Aliya Kerimbekova
Course Code: BDA350

Adds methods insert and remove to insert or remove an item
at a given position in the array.

An Array is a restricted list whose clients can use
only [], len, iter, and str.

To instantiate, use

<variable> = array(<capacity>, <optional fill value>)

The fill value is None by default.
"""


class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue=None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self._items = list()
        self._logicalSize = 0
        # Track the capacity and fill value for adjustments later
        self._capacity = capacity
        self._fillValue = fillValue
        for count in range(capacity):
            self._items.append(fillValue)
            if fillValue is not None:  # change the logical size if fill value is not None
                self._logicalSize += 1

    def __len__(self):
        """-> The capacity of the array."""
        return len(self._items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self._items)

    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self._items)

    def __getitem__(self, index):
        """Subscript operator for access at index.
        Precondition: 0 <= index < size()"""
        if index < 0 or index >= self.size():
            raise (IndexError, "Array index out of bounds")
        return self._items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index.
        Precondition: 0 <= index < size()"""
        if index < 0 or index >= self._capacity:
            raise (IndexError, "Array index out of bounds")
        if self._items[index] is None:  # add plus 1 to logical size if items was set to None value
            self._logicalSize += 1
        self._items[index] = newItem

    def size(self):
        """-> The number of items in the array."""
        return self._logicalSize

    def grow(self):
        """Increases the physical size of the array if necessary."""
        if self._logicalSize == len(self._items):  # add a constraint

            for i in range(self._capacity):
                self._items.append(self._fillValue)  # double an array
                if self._fillValue is not None:  # change the logical size if fill value is other than None
                    self._logicalSize += 1
            self._capacity = self._capacity * 2  # double the capacity

        else:
            print('No need to increase the size of an Array.')

    def __grow(self):
        """A private grow method with no constraints; used in insert function"""
        for i in range(self._capacity):
            self._items.append(self._fillValue)
        self._capacity = self._capacity * 2

    def shrink(self):
        """Decreases the physical size of the array if necessary."""
        if self._capacity % 2 == 1:  # check if capacity is odd and make sufficient changes
            temp_capacity = self._capacity/2 + 0.5
        else:
            temp_capacity = self._capacity/2

        if self._logicalSize < temp_capacity:
            self._capacity = int(temp_capacity)  # shrink the size by half but not below the default capacity
            self._items = self._items[0:self._capacity]  # remove those garbage cells from the underlying list
        else:
            print('No need to decrease the size of an Array.')

    def insert(self, index, newItem):
        """Inserts item at index in the array."""
        # check how many times we need to use grow to satisfy index attribute
        while self._logicalSize == self._capacity or index > self._capacity-1:
            self.__grow()

        if index < 0:
            raise (IndexError, "Array index out of bounds")
        elif self._items[index] is None:
            self._items[index] = newItem  # set item if a value with provided index is None

        else:
            for i in range(self._logicalSize, index, -1):  # move values
                self._items[i] = self._items[i - 1]
        self._items[index] = newItem
        self._logicalSize += 1

    def remove(self, index):
        """Removes and returns item at index in the array.
        Precondition: 0 <= index < size()"""
        item = self._items[index]
        if index <= 0 or index > self.size():  # add a constraint
            raise (IndexError, "Array index out of bounds")
        for i in range(index, self._capacity):
            try:
                self._items[i] = self._items[i + 1]
            except IndexError:
                self._items[self._capacity-1] = self._fillValue

        self._logicalSize -= 1
        return item


def main():
    """Test code for modified Array class."""
    a = Array(5)
    print("Physical size:", len(a))
    print("Logical size:", a.size())
    print("Items:", a)
    for item in range(4):
        a.insert(0, item)
    print("Items:", a)
    print("\nInserting a number into the array:\n")
    a.insert(1, 77)
    print("Items:", a)
    print("\nInserting a number into the array and doubling the size of the array:\n")

    a.insert(5, 10)
    print("Items:", a)
    print("\nRemoving from the array:\n")
    print("The number that is removed is:", a.remove(3))
    print("Items:", a)


if __name__ == "__main__":
    main()
