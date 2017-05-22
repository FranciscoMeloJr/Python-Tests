class Node(object):
    def __init__(self, id, data = []):
        self.id = id
        self.data = data
        self.children = []
        self.parent = []

    def add_child(self, obj):
        self.children.append(obj)

    def print_data(self):
        print (self.data)

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

"Main function"
def main():
    n = Node(0, 27)
    m = Node(0, 27)
    n.add_child(m)
    list = n.get_children()
    print (list[0])


"This function will create the file"
"graph { a -- b; b -- c; a -- c; d -- c; e -- c; e -- a; }"
def tree_to_file():
    gabrielmariachi@gmail.com
