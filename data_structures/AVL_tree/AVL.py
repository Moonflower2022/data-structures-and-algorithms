# elements on the left are less
# duplicate values allowed

class Node:
    def __init__(self, value, frequency=1, left_node=None, right_node=None) -> None:
        self.value = value
        self.frequency = frequency
        self.left_node = left_node
        self.right_node = right_node

    def __str__(self) -> str:
        return f"<AVLNode object; value: {self.value}, frequency: {self.frequency}, left_node: {self.left_node}, right_node: {self.right_node}>"

class AVLNode(Node):
    def __init__(self, value, parent=None, frequency=1, left_node=None, right_node=None, height=1) -> None:
        super().__init__(value, frequency=frequency, left_node=left_node, right_node=right_node)
        self.height = height # definition: max(self.left_node.height, self.right_node.height) + 1
        self.parent = parent
        self.balancing_factor = 0 # definition: self.right_node.height - self.left_node.height

    def __str__(self) -> str:
        return super().__str__()[:-1]  + f", height: {self.height}>"

class AVLTree():
    def __init__(self, root) -> None:
        self.root = root
    
    def insert(self, value, node=None):
        if node == None:
            node = self.root

        if node.value == value:
            node.frequency += 1
        elif value > node.value:
            if node.right_node == None:
                node.right_node = AVLNode(value, parent=node)
                self.update_height(node)
                self.update_balancing_factor(node)
            else:
                self.insert(value, node=node.right_node)
        elif value < node.value:
            if node.left_node == None:
                node.left_node = AVLNode(value, parent=node)
                self.update_height(node)
                self.update_balancing_factor(node)
            else:
                self.insert(value, node=node.left_node)

    def find_min(self, node=None):
        if node == None:
            node = self.root
        if node.left_node:
            return self.find_min(node=node.left_node)
        return node.value

    def update_height(self, node) -> None:
        if node.left_node == None and node.right_node == None:
            raise Exception("called update_height on node with no children")
        
        node.height = max(0 if node.left_node == None else node.left_node.height, 0 if node.right_node == None else node.right_node.height) + 1

        if node.parent: 
            self.update_height(node.parent)

    def update_balancing_factor(self, node) -> None:
        if node.left_node == None and node.right_node == None:
            raise Exception("called update_height on node with no children")
        node.balancing_factor = (0 if node.right_node == None else node.right_node.height) - (0 if node.left_node == None else node.left_node.height)

        if node.parent: 
            self.update_balancing_factor(node.parent)

        if abs(node.balancing_factor) > 1:
            self.rebalance(node)

    def rebalance(self, node):
        higher_child = AVLTree._higher_subtree_child(node)
    
        if higher_child == node.left_node:
            if node.left_node.balancing_factor <= 0:
                ret = self.rotate_right(node, node.left_node)
                self.assign(node, ret)

            else: # node.left_node.balancing_factor > 0:
                node1 = self.rotate_left(node.left_node, node.left_node.right_node)
                self.assign(node.left_node, node1)
                node2 = self.rotate_right(node, node.left_node)
                self.assign(node, node2)

        else: # higher_subtree_child == node.right_node:
            if node.right_node.balancing_factor >= 0:
                ret = self.rotate_left(node, node.right_node)
                self.assign(node, ret)
            else: # node.left_node.balancing_factor < 0:
                node1 = self.rotate_right(node.right_node, node.right_node.left_node)
                self.assign(node.right_node, node1)
                node2 = self.rotate_left(node, node.right_node)
                self.assign(node, node2)

    def assign(self, node, value):
        if node == self.root:
            self.root = value
        else:
            is_left_child = True if node.parent.value > node.value else False
            if is_left_child:
                node.parent.left_node = value
            else:
                node.parent.right_node = value
            
    def _higher_subtree_child(node):
        if node.left_node == None and node.right_node == None:
            raise Exception("called _higher_subtree_child on node with no children")
        if node.left_node != None and node.right_node != None:
            return node.left_node if node.left_node.height >= node.right_node.height else node.right_node
        elif node.left_node != None:
            return node.left_node
        else: # self.right_node != None
            return node.right_node
        
    def rotate_left(self, X, Z):
        # look at rotate_left.png
        # middle: t23

        is_root = X == self.root

        middle = Z.left_node
        X.right_node = middle
        if middle != None:
            middle.parent = X
        Z.left_node = X
        if is_root:
            self.root = Z
            Z.parent = None
        X.parent = Z
        if Z.balancing_factor == 0:
            X.balancing_factor = 1
            Z.balancing_factor = -1
        else:
            X.balancing_factor = 0
            Z.balancing_factor = 0
        return Z
    
    def rotate_right(self, X, Z):
        # rotate_left.png but flipped on the vertical axis

        is_root = X == self.root

        middle = Z.right_node
        X.left_node = middle
        if middle != None:
            middle.parent = X
        Z.right_node = X
        if is_root:
            self.root = Z
            Z.parent = None
        X.parent = Z
        if Z.balancing_factor == 0:
            X.balancing_factor = -1
            Z.balancing_factor = 1
        else:
            X.balancing_factor = 0
            Z.balancing_factor = 0
        return Z