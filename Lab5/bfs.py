class Node:
    def __init__(self,data):
        self.data = data
        self.children = []
    
    def add_child(self,child):
        self.children.append(child)
    
class Tree:
    def __init__(self,root):
        self.root = root

    def bfs(self):
        if self.root is None:
            return
        print(f'{self.root.data}',end='')
        explore = self.root.children
        
        while(len(explore) != 0):
            current = explore.pop(0)
            explore += current.children
            print(f'->{current.data}',end='')
        print("\n")

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")
i = Node("I")

a.add_child(b)
a.add_child(c)

b.add_child(d)
b.add_child(e)
b.add_child(f)

c.add_child(g)
c.add_child(h)

d.add_child(i)

tree = Tree(a)
tree.bfs()
