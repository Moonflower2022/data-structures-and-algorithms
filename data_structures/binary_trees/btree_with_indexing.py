import graphviz

# elements on the left are less
# duplicate values allowed
# using indexing in an array

# YOOO I talked to wes this is really dumb and pointlesss

class Node:
    def __init__(self, value, left_pointer=None, right_pointer=None) -> None:
        self.value = value
        self.frequency = 1
        self.left_pointer = left_pointer
        self.right_pointer = right_pointer

    def __str__(self) -> str:
        return f"<AVLNode object; value: {self.value}, frequency: {self.frequency}, left_pointer: {self.left_pointer}, right_pointer: {self.right_pointer}>"
    
class BinaryTree:
    def __init__(self) -> None:
        self.tree = []
        
    def __str__(self) -> str:
        return str([node.__str__() for node in self.tree])
    
    def index(self, ele): # -1 if not found, pointer if found ig
        pass

    def travel(self, index, value):
        if self.tree[index].value == value:
            self.tree[index].frequency += 1

        elif value > self.tree[index].value:
            if self.tree[index].right_pointer == None:
                self.tree[index].right_pointer = len(self.tree)
                self.tree.append(Node(value))
            else:
                self.travel(self.tree[index].right_pointer, value)
        elif value < self.tree[index].value:
            if self.tree[index].left_pointer == None:
                self.tree[index].left_pointer = len(self.tree)
                self.tree.append(Node(value))
            else:
                self.travel(self.tree[index].right_pointer, value)

    def insert(self, value) -> None:
        if len(self.tree) == 0:
            self.tree.append(Node(value))
            return
        self.travel(0, value)

tree = BinaryTree()

tree.insert(4)
tree.insert(5)
tree.insert(3)


print(tree)