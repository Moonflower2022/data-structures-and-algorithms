# elements on the left are less
# duplicate values allowed

# import sys

# sys.path.append("../")

# from ..binary_trees.btree import Node

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

    def update_height(self) -> None:
        if self.left_node == None and self.right_node == None:
            raise Exception("called update_height on node with no children")
        if self.left_node != None and self.right_node != None: # and self.right_node != None
            self.height = max(self.left_node.height, self.right_node.height) + 1
        elif self.left_node != None:
            self.height = self.left_node.height + 1
        else: # self.right_node != None
            self.height = self.right_node.height + 1

        if self.parent: 
            self.parent.update_height()

    def update_balancing_factor(self) -> None:
        if self.left_node == None and self.right_node == None:
            raise Exception("called update_height on node with no children")
        if self.left_node != None and self.right_node != None: # and self.right_node != None
            self.balancing_factor = self.right_node.height - self.left_node.height
        elif self.left_node != None:
            self.balancing_factor = -self.left_node.height
        else: # self.right_node != None
            self.balancing_factor = self.right_node.height

        if self.parent: 
            self.parent.update_balancing_factor()

    def __str__(self) -> str:
        return super().__str__()[:-1]  + f", height: {self.height}>"
    
def AVL_insert(node, value):
    if node.value == value:
        node.frequency += 1
    elif value > node.value:
        if node.right_node == None:
            node.right_node = AVLNode(value, parent=node)
            node.update_height()
            node.update_balancing_factor()
        else:
            AVL_insert(node.right_node, value)
    elif value < node.value:
        if node.left_node == None:
            node.left_node = AVLNode(value, parent=node)
            node.update_height()
            node.update_balancing_factor()
        else:
            AVL_insert(node.left_node, value)

def rotate_left(X, Z):
    # look at rotate_left.png
    # middle: t23

    middle = Z.left_node
    X.right_node = middle
    if middle != None:
        middle.parent = X
    Z.left_node = X
    X.parent = Z
    if Z.balancing_factor == 0:
        X.balancing_factor = 1
        Z.balancing_factor = -1
    else:
        X.balancing_factor = 0
        Z.balancing_factor = 0
    return Z

def rotate_right(X, Z):
    # rotate_left.png but flipped on the vertical axis

    middle = Z.right_node
    X.left_node = middle
    if middle != None:
        middle.parent = X
    Z.right_node = X
    X.parent = Z
    if Z.balancing_factor == 0:
        X.balancing_factor = -1
        Z.balancing_factor = 1
    else:
        X.balancing_factor = 0
        Z.balancing_factor = 0
    return Z

def find_min(root):
    if root.left_node:
        return find_min(root.left_node)
    return root.value