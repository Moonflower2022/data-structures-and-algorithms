from AVL_better import AVLTree
import graphviz
import os
import random

numbers = list(range(29))

random.shuffle(numbers)

tree = AVLTree()

for i in range(len(numbers)):
    tree.insert(numbers[i])

print(tree.find_min())

tree.delete(5)
tree.delete(6)

def visualize_AVL_tree(tree):
    # does not show frequency

    dot = graphviz.Digraph()
    dot.node(str(tree.root.value))

    def add_nodes_and_edges(node):
        if node.left_node:
            dot.node(str(node.left_node.value))
            dot.edge(str(node.value), str(node.left_node.value))
            add_nodes_and_edges(node.left_node)
        if node.right_node:
            dot.node(str(node.right_node.value))
            dot.edge(str(node.value), str(node.right_node.value))
            add_nodes_and_edges(node.right_node)

    add_nodes_and_edges(tree.root)

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'AVL_tree')

    dot.render(filename, view=True, format='png')

visualize_AVL_tree(tree)