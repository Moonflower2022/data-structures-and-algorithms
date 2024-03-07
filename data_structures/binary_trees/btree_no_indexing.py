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
    
def insert(root, value):
    if root.value == value:
        root.frequency += 1
    elif value > root.value:
        if root.right_node == None:
            root.right_node = Node(value)
        else:
            insert(root.right_node, value)
    elif value < root.value:
        if root.left_node == None:
            root.left_node = Node(value)
        else:
            insert(root.left_node, value)

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

root = Node(6)
insert(root, 8)
insert(root, 4)
insert(root, 5)
insert(root, 2)
insert(root, 1)

print(find_min(root))

visualize_binary_tree(root)