import graphviz

# elements on the left are less
# duplicate values allowed

class Node:
    def __init__(self, value, left_node=None, right_node=None) -> None:
        self.value = value
        self.frequency = 1
        self.left_node = left_node
        self.right_node = right_node

    def __str__(self) -> str:
        return f"<AVLNode object; value: {self.value}, frequency: {self.frequency}, left_node: {self.left_node}, right_node: {self.right_node}>"

class AVLNode(Node):
    def __init__(self, value, parent, left_node=None, right_node=None, left_height=None, height=None, right_height=None) -> None:
        super().__init__(value, left_node, right_node)
        self.left_height = left_height
        self.right_height = right_height
        self.height = height # definition: max(left_height, right_height)
        self.parent = parent

    def __str__(self) -> str:
        return super().__str__()[:-1]  + f", left_height: {self.left_height}, right_height: {self.right_height}>"
    
def insert(node, value):
    if node.value == value:
        node.frequency += 1
    elif value > node.value:
        if node.right_node == None:
            node.right_node = AVLNode(value, node)
            node.right_height += 1
            increment_parent_height(node, "right")
        else:
            insert(node.right_node, value)
    elif value < node.value:
        if node.left_node == None:
            node.left_node = AVLNode(value, node)
            node.left_height += 1
            increment_parent_height(node, "left")
        else:
            insert(node.left_node, value)

def increment_parent_height(node, side):
    if side == "left":
        node.parent.left_height += 1
    else: # side == "right"
        node.parent.right_height += 1

def AVL_insert(root, value):
    pass

def find_min(root):
    if root.left_node:
        return find_min(root.left_node)
    return root.value

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
    dot.render('binary_tree', view=True, format='png')

root = AVLNode(9, None)

print(root)

'''

root = Node(6)
insert(root, 8)
insert(root, 4)
insert(root, 5)
insert(root, 2)
insert(root, 1)

print(find_min(root))

visualize_binary_tree(root)
'''