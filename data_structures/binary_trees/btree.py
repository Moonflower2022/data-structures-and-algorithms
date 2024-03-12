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