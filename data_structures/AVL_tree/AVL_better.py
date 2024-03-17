# elements on the left are less
# duplicate values not allowed

class Node:
    def __init__(self, value, frequency=1, left_node=None, right_node=None) -> None:
        self.value = value
        self.left_node = left_node
        self.right_node = right_node
        self.frequency = frequency

    def __str__(self) -> str:
        return f"<AVLNode object; value: {self.value}, frequency: {self.frequency}, left_node: {self.left_node}, right_node: {self.right_node}>"

class AVLNode(Node):
    def __init__(self, value, left_node=None, right_node=None, height=1) -> None:
        super().__init__(value, left_node=left_node, right_node=right_node)
        self.height = height # 1 + definition: max(self.left_node.height, self.right_node.height)

    def __str__(self) -> str:
        return super().__str__()[:-1]  + f", height: {self.height}>"

class AVLTree():
    def __init__(self, root=None) -> None:
        self.root = root

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance_factor(self, node):
        return self.height(node.right_node) - self.height(node.left_node)

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left_node), self.height(node.right_node))
        
    def rotate_left(self, X, Z):
        # look at rotate_left.png
        # middle: t23

        # Z is the right_node of X

        middle = Z.left_node
        X.right_node = middle
        Z.left_node = X

        self.update_height(X)
        self.update_height(Z)

        return Z
    
    def rotate_right(self, X, Z):
        # rotate_left.png but flipped on the vertical axis

        # Z is the left node of X

        middle = Z.right_node
        X.left_node = middle
        Z.right_node = X

        self.update_height(X)
        self.update_height(Z)

        return Z
    
    def rebalance(self, node):
        self.update_height(node)

        balance = self.balance_factor(node)
    
        if balance < -1 and self.balance_factor(node.left_node) <= 0:
            return self.rotate_right(node, node.left_node)

        if balance < -1 and self.balance_factor(node.left_node) > 0:
            node.left_node = self.rotate_left(node.left_node, node.left_node.right_node)
            return self.rotate_right(node, node.left_node)

        if balance > 1 and self.balance_factor(node.right_node) >= 0:
            return self.rotate_left(node, node.right_node)
        
        if balance > 1 and self.balance_factor(node.right_node) < 0:
            node.right_node = self.rotate_right(node.right_node, node.right_node.left_node)
            return self.rotate_left(node, node.right_node)
        
        return node
        
    def insert(self, value):
        self.root = self.updated_tree(value, node=self.root)
    
    def updated_tree(self, value, node):
        if node == None:
            return AVLNode(value)

        if value < node.value:
            node.left_node = self.updated_tree(value, node=node.left_node)
        elif value > node.value:
            node.right_node = self.updated_tree(value, node=node.right_node)
        else:
            node.frequency += 1
        
        return self.rebalance(node)

    def find_min(self, node=None):
        if node == None:
            node = self.root
        if node.left_node:
            return self.find_min(node=node.left_node)
        return node.value
    
    def delete(self, value):
        self.root = self.delete_node(value, self.root)

    def delete_node(self, value, node):
        if node is None:
            return None

        if value < node.value:
            node.left_node = self.delete_node(value, node.left_node)
        elif value > node.value:
            node.right_node = self.delete_node(value, node.right_node)
        else:
            # Case 1: Node has no children
            if node.left_node is None and node.right_node is None:
                del node
                return None
            # Case 2: Node has one child
            elif node.left_node is None:
                temp = node.right_node
                del node
                return temp
            elif node.right_node is None:
                temp = node.left_node
                del node
                return temp
            # Case 3: Node has two children
            else:
                successor_value = self.find_min(node.right_node)
                node.value = successor_value
                node.right_node = self.delete_node(successor_value, node.right_node)

        return self.rebalance(node)
    