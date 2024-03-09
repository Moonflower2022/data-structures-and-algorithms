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
    def __init__(self, value, parent, frequency=1, left_node=None, right_node=None, height=1) -> None:
        super().__init__(value, frequency, left_node, right_node)
        self.height = height # definition: max(self.left_node.height, self.right_node.height) + 1
        self.parent = parent

    def update_height(self):
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

    def __str__(self) -> str:
        return super().__str__()[:-1]  + f", height: {self.height}>"
    
def insert(node, value):
    if node.value == value:
        node.frequency += 1
    elif value > node.value:
        if node.right_node == None:
            node.right_node = AVLNode(value, node)
            node.update_height()
        else:
            insert(node.right_node, value)
    elif value < node.value:
        if node.left_node == None:
            node.left_node = AVLNode(value, node)
            node.update_height()
        else:
            insert(node.left_node, value)


def AVL_insert(root, value):
    pass

def find_min(root):
    if root.left_node:
        return find_min(root.left_node)
    return root.value

root = AVLNode(9, None)

insert(root, 8)
insert(root, 4)
insert(root, 5)
insert(root, 2)
insert(root, 1)

print(root)

print(find_min(root))

import graphviz
import os

def visualize_binary_tree(root):
    # does not show frequency

    dot = graphviz.Digraph()
    dot.node(str(root.value))

    def add_nodes_and_edges(node):
        if node.left_node:
            dot.node(str(node.left_node.value))
            dot.edge(str(node.value), str(node.left_node.value))
            add_nodes_and_edges(node.left_node)
        if node.right_node:
            dot.node(str(node.right_node.value))
            dot.edge(str(node.value), str(node.right_node.value))
            add_nodes_and_edges(node.right_node)

    add_nodes_and_edges(root)

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'AVL_tree')

    dot.render(filename, view=True, format='png')

visualize_binary_tree(root)