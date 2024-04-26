"""
File: binarytree.py

Adds methods to return the hieght of a tree and a list containing
its leaves.

A binary tree ADT

Example initializations:
anEmptyTree = BinaryTree.THE_EMPTY_TREE
aNonemptyTree = BinaryTree("One item")

"""

from queue import LinkedQueue


class EmptyTree(object):
    """Represents an empty tree."""

    # supported methods

    def isEmpty(self):
        return True

    def __str__(self):
        return ""

    def __iter__(self):
        """Iterator for the tree."""
        return iter([])

    def preorder(self, lyst):
        return

    def inorder(self, lyst):
        return

    def postorder(self, lyst):
        return

    # Methods not supported but in the interface for all
    # binary trees

    def getRoot(self):
        raise (AttributeError, "Empty tree")

    def getLeft(self):
        raise (AttributeError, "Empty tree")

    def getRight(self):
        raise (AttributeError, "Empty tree")

    def setRoot(self, item):
        raise (AttributeError, "Empty tree")

    def setLeft(self, tree):
        raise (AttributeError, "Empty tree")

    def setRight(self, tree):
        raise (AttributeError, "Empty tree")

    def removeLeft(self):
        raise (AttributeError, "Empty tree")

    def removeRight(self):
        raise (AttributeError, "Empty tree")

    def height(self):
        return -1

    def leaves(self):
        return []


class BinaryTree(object):
    """Represents a nonemoty binary tree."""

    # Singleton for all empty tree objects
    THE_EMPTY_TREE = EmptyTree()

    def __init__(self, item):
        """Creates a tree with
        the given item at the root."""
        self._root = item
        self._left = BinaryTree.THE_EMPTY_TREE
        self._right = BinaryTree.THE_EMPTY_TREE

    def isEmpty(self):
        return False

    def getRoot(self):
        return self._root

    def getLeft(self):
        # Returns the left subtree. Precondition: T is not an empty tree.
        return self._left

    def getRight(self):
        # Returns the right subtree. Precondition: T is not an empty tree.
        return self._right

    def setRoot(self, item):
        self._root = item

    def setLeft(self, tree):
        # Sets the left subtree to tree. Precondition: T is not an empty tree.
        self._left = tree

    def setRight(self, tree):
        # Sets the right subtree to tree. Precondition: T is not an empty tree.
        self._right = tree

    def removeLeft(self):
        """Removes and returns the left subtree.
        Precondition: T is not an empty tree. Postcondition: the left subtree is empty."""
        left = self._left
        self._left = BinaryTree.THE_EMPTY_TREE
        return left

    def removeRight(self):
        """Removes and returns the right subtree.
        Precondition: T is not an empty tree. Postcondition: the right subtree is empty."""
        right = self._right
        self._right = BinaryTree.THE_EMPTY_TREE
        return right

    def __str__(self):
        """Returns a string representation of the tree
        rotated 90 degrees to the left."""

        def strHelper(tree, level):
            result = ""
            if not tree.isEmpty():
                result += strHelper(tree.getRight(), level + 1)
                result += "| " * level
                result += str(tree.getRoot()) + "\n"
                result += strHelper(tree.getLeft(), level + 1)
            return result

        return strHelper(self, 0)

    def __iter__(self):
        """Iterator for the tree."""
        lyst = []
        self.inorder(lyst)
        return iter(lyst)

    def preorder(self, lyst):
        """Adds items to lyst during
        a preorder traversal."""
        lyst.append(self.getRoot())
        self.getLeft().preorder(lyst)
        self.getRight().preorder(lyst)

    def inorder(self, lyst):
        """Adds items to lyst during
        an inorder traversal."""
        self.getLeft().inorder(lyst)
        lyst.append(self.getRoot())
        self.getRight().inorder(lyst)

    def postorder(self, lyst):
        """Adds items to lystduring
        a postorder traversal."""
        self.getLeft().postorder(lyst)
        self.getRight().postorder(lyst)
        lyst.append(self.getRoot())

    def levelorder(self, lyst):
        """Adds items to lyst during
        a levelorder traversal."""
        levelsQueue = LinkedQueue()
        levelsQueue.enqueue(self)
        while not levelsQueue.isEmpty():
            node = levelsQueue.dequeue()
            lyst.append(node.getRoot())
            left = node.getLeft()
            right = node.getRight()
            if not left.isEmpty():
                levelsQueue.enqueue(left)
            if not right.isEmpty():
                levelsQueue.enqueue(right)

    def height(self):
        """
        Set left to point to the left subtree
        Set right to point to the right subtree
        You may use getLeft() or getRight()

        If you have reached the leaf, return 0.
        Otherwise, recursively add 1 to the maximum height.
        """
        if self is None:
            return -1
        else:
            left = self.getLeft().height()
            right = self.getRight().height()
            if left > right:
                return left + 1
            else:
                return right + 1

    def leaves(self):
        """
        Set left to point to the left subtree
        Set right to point to the right subtree
        You may use getLeft() or getRight()

        If you have reached the leaf, return it (call getRoot).
        Otherwise, recursively add the leaves on the left subtree and the right subtree
        """
        if self.isEmpty():
            return []
        elif self.getLeft().isEmpty() and self.getRight().isEmpty():
            return [self.getRoot()]
        else:
            return self.getLeft().leaves() + self.getRight().leaves()


def main():
    # Create initial leaf nodes
    a = BinaryTree("A")
    b = BinaryTree("B")
    c = BinaryTree("C")
    d = BinaryTree("D")
    e = BinaryTree("E")
    f = BinaryTree("F")
    g = BinaryTree("G")

    # Build the tree from the bottom up, where
    # d is the root node of the entire tree

    # Build and set the left subtree of d
    b.setLeft(a)
    b.setRight(c)
    d.setLeft(b)

    # Build and set the right subtree of d
    f.setLeft(e)
    f.setRight(g)
    d.setRight(f)

    print("Height of 2:", d.height())
    print("Height of 0:", c.height())
    print("Height of 0:", a.height())
    print("Height of -1:", BinaryTree.THE_EMPTY_TREE.height())

    print("Leaves:", d.leaves())


if __name__ == "__main__":
    main()
