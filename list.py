
from arrays import Array


class ArrayList(object):
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._items = Array(ArrayList.DEFAULT_CAPACITY)
        self._size = 0
        self._last = -1

    def isEmpty(self):
        return self._size == 0

    def __len__(self):
        """Returns the number of items in the stack."""
        return self._size

    def __str__(self):
        return str(self._items)

    def _grow(self):
        """ Private method to make an array bigger if necessary"""
        new_array = Array(self._size * 2)
        for i in range(len(self._items)):
            new_array[i] = self._items[i]
        self._items = new_array

    def append(self, item):
        if self._size == len(self._items):  # resize of necessary
            self._grow()
        self._items[self._last + 1] = item
        self._size += 1
        self._last += 1
        return item

    def insert(self, item, index):
        if index <= 0 or index > self._size:  # add a constraint
            raise (IndexError, "Array index out of bounds")
        if self._size == len(self._items):
            self._grow()
        for i in range(self._size, index, -1):  # move values
            self._items[i] = self._items[i - 1]
        self._items[index] = item
        self._size += 1
        self._last += 1
        return item

    def remove(self, index):
        removed_item = self._items[index]
        if index <= 0 or index > self._size:  # add a constraint
            raise (IndexError, "Array index out of bounds")
        for i in range(index, self._size):
            try:
                self._items[i] = self._items[i + 1]
            except IndexError:
                self._items[self._size - 1] = None
        self._size -= 1
        self._last -= 1
        return removed_item

    def search(self, item):
        for i in self._items:
            if i == item:
                return True
        return False


def main():
    indexed = ArrayList()
    indexed.append("KS944RUR")
    indexed.append("GT567UYC")
    indexed.append("TYH7653N")
    indexed.append("WER577D8")

    print(indexed, "\n")

    indexed.insert("YH67FG54", 2)
    print(indexed, "\n")

    indexed.remove(1)

    print(indexed, "\n")

    if indexed.search("U78G77"):
        print("Item is found.")
    else:
        print('Item is not found.')

    if indexed.search("YH67FG54"):
        print("Item is found.")
    else:
        print("Item is not found.")


if __name__ == "__main__":
    main()
