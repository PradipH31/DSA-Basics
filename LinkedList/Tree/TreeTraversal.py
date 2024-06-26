class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None


def in_order(root: Node):
    if root:
        in_order(root.left)
        print(root.value, end='-')
        in_order(root.right)


def pre_order(root: Node):
    if root:
        print(root.value, end='-')
        in_order(root.left)
        in_order(root.right)


def post_order(root: Node):
    if root:
        in_order(root.left)
        in_order(root.right)
        print(root.value, end='-')


def breadth_first(root: Node):
    queue = [root]
    while len(queue) != 0:
        curr = queue.pop(0)
        print(curr.value, end='-')
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)


root = Node(65)
root.left = Node(52)
root.left.left = Node(46)
root.left.right = Node(55)
root.right = Node(68)
root.right.left = Node(40)
root.right.right = Node(99)

print(pre_order(root), '')
print(in_order(root), '')
print(post_order(root), '')
print(breadth_first(root), '')
