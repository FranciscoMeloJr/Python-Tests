#Profile Data:
class ProfileData(object):
    def __init__(self, id, data=[]):
        self.data = data

#Node:
class Node(object):
    def __init__(self, id, data = []):
        self.id = id
        self.data = data
        self.children = []
        self.parent = []
        self.times = 1


    def get_label(self):
        return self.id

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

    def get_times(self):
        return self.times

    def increment(self):
        self.times = self.times +1

    def set_profile_data(self, ProfileData):
        self.PD = ProfileData
        
"Test function"
def test():
    n = Node(0, 27)
    m = Node(0, 27)
    n.add_child(m)
    list = n.get_children()
    print (list[0])


"This function will create the file"
"graph { a -- b; b -- c; a -- c; d -- c; e -- c; e -- a; }"
def tree_to_file():
    return 0