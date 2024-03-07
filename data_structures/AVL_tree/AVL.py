# elements on the right are less
# no duplicate values

class AVLNode:
    def __init__(self, value, left_pointer, right_pointer, balance_factor) -> None:
        self.value = value
        self.left_pointer = left_pointer
        self.right_pointer = right_pointer
        self.balance_factor = balance_factor

    def __str__(self) -> str:
        return f"<AVLNode object; value: {self.value}, left_pointer: {self.left_pointer}, right_pointer: {self.right_pointer}, balance_factor: {self.balance_factor}>"
    
class AVLTree:
    def __init__(self) -> None:
        self.tree = []
        
    def __str__(self) -> str:
        return str([node.__str__() for node in self.tree])
    
    def find(self, ele): # -1 if not found, ______ if found
        pass

    def insert(self, value) -> None:
        if len(self.tree == 0):
            self.tree.append(AVLNode(value, None, None, 0))

        
        pass

print(AVLTree())