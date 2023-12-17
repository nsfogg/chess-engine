# Nick Fogg
# 12/17/2023
# Tree data structure

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def __str__(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|--" if self.parent else ""
        ret = f"{prefix}{self.data}"
        if len(self.children) > 0:
            for child in self.children:
                self.__str__(child)
        return ret

