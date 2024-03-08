from btree import Node, insert, find_min
import os
import graphviz

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
    filename = os.path.join(dirname, 'binary_tree')

    dot.render(filename, view=True, format='png')

root = Node(6)
insert(root, 8)
insert(root, 4)
insert(root, 5)
insert(root, 2)
insert(root, 1)

print(find_min(root))

visualize_binary_tree(root)