# Traversal Tree: Preorder, Inorder, dan Postorder Secara Rekursif

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 1. Preorder Traversal (Akar, Kiri, Kanan)
def preorderTraversal(root):
    answer = []
    def preorderTraversalUtil(root, answer):
        if root is None:
            return
        answer.append(root.val)
        preorderTraversalUtil(root.left, answer)
        preorderTraversalUtil(root.right, answer)
    preorderTraversalUtil(root, answer)
    return answer

# 2. Postorder Traversal (Kiri, Kanan, Akar)
def postorderTraversal(root):
    answer = []
    def postorderTraversalUtil(root, answer):
        if root is None:
            return
        postorderTraversalUtil(root.left, answer)
        postorderTraversalUtil(root.right, answer)
        answer.append(root.val)
    postorderTraversalUtil(root, answer)
    return answer

# 3. Inorder Traversal (Kiri, Akar, Kanan)
def inorderTraversal(root):
    answer = []
    def inorderTraversalUtil(root, answer):
        if root is None:
            return
        inorderTraversalUtil(root.left, answer)
        answer.append(root.val)
        inorderTraversalUtil(root.right, answer)
    inorderTraversalUtil(root, answer)
    return answer

if __name__ == "__main__":
    # Konstruksi Tree Contoh:
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Hasil Preorder Traversal (Akar -> Kiri -> Kanan):")
    print(preorderTraversal(root))

    print("\nHasil Inorder Traversal (Kiri -> Akar -> Kanan):")
    print(inorderTraversal(root))

    print("\nHasil Postorder Traversal (Kiri -> Kanan -> Akar):")
    print(postorderTraversal(root))
