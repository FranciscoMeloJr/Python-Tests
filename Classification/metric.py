
from execution import Execution

"This function will create the runs for testing"
def create_list_Executions(tam):
    list_objects = []
    i = 0
    each = [1,1,0]
    while (i < tam):
        x = Execution(i, each)
        list_objects.append(x)
        i = i + 1

    y = [0, 0, 1]
    x = Execution(i, y)
    list_objects.append(x)
    return list_objects

"Class to keep the groups"
class Group(object):
    """A simple example class"""
    id = -1
    executions_ids = []
    group_name = ""
    metric_name = ""

    def __init__(self, id):
        self.id = id

    def __init__(self, id, group_name, metric_name= "unknown", exe_ids = []):
        self.id = id
        self.metric_name = metric_name
        self.group_name = group_name
        self.executions_ids = exe_ids

    def add_execution(self, execution):
        self.executions_ids = execution

    def show(self):
        print (self.group_name)
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

"Class metric"
class Metric(object):
    groups = []
    name = ""
    list_executions = []
    results = []
    qtd = 0

    def __init__(self, name, groups= [], id = -1):
        self.id = id
        self.name = name
        if len(groups) > 0:
            self.create_groups(groups)
        else:
            self.groups = groups

    def set_groups(self, groups):
        self.groups = groups

    def show(self):
        print self.name
        print self.groups

    def get_qtd_groups(self):
        return len(self.groups)

    def set_list_execution(self, list):
        self.list_executions = list

    def get_executions_groups(self):
        return self.list_executions

    def get_size(self):
        return qtd

    "Returns all the results"
    def get_result(self):
        return self.results

    def get_groups(self):
        return self.groups

    "This function returns all the executions from a group"
    def get_all_executions_by_group_index(self, index):

        result = []
        for each in self.results:
            if (each[2]== index):
                result.append(each[0])

        return result

    "This function to creates the groups inside the metric"
    def create_groups(self, list_values):
        list_values = sorted(list_values)
        list_groups = []
        aux = []
        previous = list_values[0]

        for each in list_values:
            if each == previous:
                aux.append(each)
            else:
                list_groups.append(aux)
                aux = []
                aux.append(each)
            previous = each
        list_groups.append(aux)
        self.groups = list_groups
        self.qtd = len(list_values)

    "Creates a metric from an execution list"
    def create_from_execution_list(self, list_executions, index, flag):
        values = []
        matrix = []
        temp = []
        for each in list_executions:
            v = each.get_index_metrics(index)
            id = each.get_id()
            values.append(v)
            temp = [v, id]
            matrix.append(temp)

        self.create_groups(values)

        if(flag):
            print matrix

        temp = []
        result_matrix = []
        for each in matrix:
            group = self.give_value_I_will_find_group(each[0])#value
            each[1]#id
            temp = [each[1], each[0], group] #[id, value, group]
            result_matrix.append(temp)


        self.results = result_matrix

        i = 0
        list_exe_by_group = []
        while i < len(self.groups):
            temp = self.get_all_executions_by_group_index(i)
            i = i + 1
            list_exe_by_group.append(temp)

        self.list_executions = list_exe_by_group

    "This function to find the group of a variable"
    def give_value_I_will_find_group(self, value):

        i = 0
        for eachG in self.groups:
            for eachValue in eachG:
                if eachValue == value:
                    return i
            i = i + 1
        return -1


"Cross validation p1"
def take_all_groups(list_metrics):

    temp = []
    i = 0
    total = []
    for each in list_metrics:
        qtd = each.get_qtd_groups()
        i = 0
        while i < qtd:
            list_ids = each.get_all_executions_by_group_index(i)
            total.append(list_ids)
            i = i + 1

    print "total"
    print total
    return total

"Cross validation p2"
def cross(list_groups, qtd, flag):
    i = 0
    matrix = []
    while i < len(list_groups):
        b1 = list_groups[i]
        j = 0
        temp = []
        while j < len(list_groups):
            b2 = list_groups[j]
            result = len(set(b1).intersection(b2))
            result = float(result) / float(qtd)
            if(flag):
                print "b1 " + str(b1) + " b2 " +  str(b2) + " " + str(result)
            temp.append(result)
            j = j + 1
        matrix.append(temp)
        i = i + 1

    return matrix

"Function to print"
def print_matrix(matrix):
    for row in matrix:
        for collumn in row:
            print collumn
        print "\n"

"This function creates the metrics from the executions"
def create_list_metrics(list):
    list_metrics = []

    m1 = Metric("Velocidade")
    m1.create_from_execution_list(list, 0, False)
    list_metrics.append(m1)
    print "Velocidade"
    print m1.get_executions_groups()

    m2 = Metric("Potencia")
    m2.create_from_execution_list(list, 1, False)
    list_metrics.append(m2)
    print "Potencia"

    print m2.get_executions_groups()

    m3 = Metric("Camisa")
    m3.create_from_execution_list(list, 2, False)
    list_metrics.append(m3)
    print "Camisa"
    print m3.get_executions_groups()

    return list_metrics

"Main function"
def main():
    list = create_list_Executions(10)
    list_metrics = create_list_metrics(list)


    print "Cross validation"
    total = take_all_groups(list_metrics)
    print cross(total, 11, False)


main()