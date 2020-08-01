class BSTNode:
    def __init__(self, value):
        self.value = value
        self.length = 0
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        current_node = self

        while current_node is not None:
            # print('current_node', current_node.value)
            if value <= current_node.value:
                if current_node.left is None:
                    current_node.left = BSTNode(value)
                    current_node.length += 1
                    return
                else:
                    # print('left child', current_node.left.value)
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = BSTNode(value)
                    current_node.length += 1
                    return
                else:
                    # print('right child', current_node.right.value)
                    current_node = current_node.right

    def contains(self, target):
        current_node = self

        while current_node is not None:
            if target < current_node.value:
                if current_node.left is None:
                    return False
                else:
                    # print('left child', current_node.left.value)
                    current_node = current_node.left
            elif target > current_node.value:
                if current_node.right is None:
                    return False
                else:
                    # print('right child', current_node.right.value)
                    current_node = current_node.right
            else:
                return True