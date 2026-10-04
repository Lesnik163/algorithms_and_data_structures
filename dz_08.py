from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        return self._after_insert(node)

    def _after_insert(self, node):
        return node

    def search(self, value):
        node = self.root
        while node is not None:
            if value == node.value:
                return node
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return None


def bfs(tree):
    if tree.root is None:
        return []

    result = []
    nodes = deque([tree.root])
    while nodes:
        node = nodes.popleft()
        result.append(node.value)
        if node.left is not None:
            nodes.append(node.left)
        if node.right is not None:
            nodes.append(node.right)
    return result


def preorder(tree):
    return _preorder(tree.root)


def _preorder(node):
    if node is None:
        return []
    return [node.value] + _preorder(node.left) + _preorder(node.right)


def inorder(tree):
    return _inorder(tree.root)


def _inorder(node):
    if node is None:
        return []
    return _inorder(node.left) + [node.value] + _inorder(node.right)


def postorder(tree):
    return _postorder(tree.root)


def _postorder(node):
    if node is None:
        return []
    return _postorder(node.left) + _postorder(node.right) + [node.value]


class AVLTree(BinaryTree):
    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def rebalance(self, node):
        self._update_height(node)
        balance = self._balance_factor(node)

        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def _after_insert(self, node):
        return self.rebalance(node)


print("Задание 1. Вставка и поиск")
tree = BinaryTree()
for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    tree.insert(value)

print("корень:", tree.root.value)
found = tree.search(6)
print("поиск 6:", found.value if found else None)
print("поиск 100:", tree.search(100))

print("\nЗадание 2. Обход в ширину (BFS)")
print(bfs(tree))

print("\nЗадание 3. Обходы в глубину (DFS)")
print("preorder:", preorder(tree))
print("inorder:", inorder(tree))
print("postorder:", postorder(tree))

print("\nЗадание 4. AVL-дерево")
avl = AVLTree()
for value in [1, 2, 3, 4, 5, 6, 7]:
    avl.insert(value)

print("inorder:", inorder(avl))
print("bfs:", bfs(avl))
print("корень:", avl.root.value, "высота:", avl.root.height)
