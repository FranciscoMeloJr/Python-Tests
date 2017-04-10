class Node(object):
    def __init__(self, id, data = []):
        self.id = id
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

    def print_data(self):
        print (self.data)

    def get_children(self):
        return self.children

"Main function"
def main():
    n = Node(0, 27)
    m = Node(0, 27)
    n.add_child(m)
    list = n.get_children()
    print (list[0])

main()