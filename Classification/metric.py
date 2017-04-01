
#Class used to control each metric
class Metric(object):
    """A simple example class"""
    id = -1
    executions_ids = []
    name = ""

    def __init__(self, id):
        self.id = id

    def __init__(self, id, name= "unknown", exe_ids = []):
        self.id = id
        self.name = name
        self.executions_ids = exe_ids

    def show(self):
        print (self.executions_ids)
        return

    def set_executions(self, executions):
        self.executions_ids = executions

    def set_name(self, name):
        self.name = name

    def get_executions(self):
        return self.executions_ids

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name


x = Metric(27, "Velocidade")