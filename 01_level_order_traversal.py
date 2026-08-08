# Algoritma Level Order Tree Traversal Menggunakan Queue

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def levelorder(root):
    """
    Melintasi pohon per tingkat (level order) menggunakan antrian Queue.
    """
    Q = queue.Queue()
    Q.put(root)
    while not Q.empty():
        node = Q.get()
        if node is None:
            continue
        print(node.data)
        Q.put(node.leftChild)
        Q.put(node.rightChild)

def insert(root, newValue):
    if root is None:
        root = BinaryTreeNode(newValue)
        return root
    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:
        root.rightChild = insert(root.rightChild, newValue)
    return root

if __name__ == "__main__":
    root = insert(None, 50)
    insert(root, 20)
    insert(root, 53)
    insert(root, 11)
    insert(root, 22)
    insert(root, 52)
    insert(root, 78)

    print("Level Order traversal of the binary tree is:")
    levelorder(root)
