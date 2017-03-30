
#Class used for classification:
class Execution(object):
    """A simple example class"""
    id = -1
    metrics = -1
    info = []
    classification = []

    def __init__(self, list):
        self.metrics = list

    def __init__(self, id, list):
        self.id = id
        self.metrics = list
        print self.metrics

    def show(self):
        print (self.metrics)
        return

    def get_metrics_1(self):
        return self.metrics[0]

    def get_index_metrics(self, index):
        return self.metrics[index]

    def print_metrics(self):
        print self.metrics

    def set_classification(self, data):
        self.classification = data

    def show(self):
        print self.id #+ " "+ self.metrics

    def __str__(self):
        str1 = ''.join(self.info)
        return str1

    def get_info(self):
        return self.info

    def get_classification(self):
        return self.classification
