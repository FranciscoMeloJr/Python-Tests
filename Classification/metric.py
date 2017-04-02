
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

    "This function returns all the executions from a group"
    def get_all_executions_by_group_index(self, index):

        result = []
        for each in self.list_executions:
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

        self.list_executions = result_matrix

    "This function to find the group of a variable"
    def give_value_I_will_find_group(self, value):

        i = 0
        for eachG in self.groups:
            for eachValue in eachG:
                if eachValue == value:
                    return i
            i = i + 1
        return -1

"This function to create a test to create executions and metrics"
def test_create_executions():
    list_executions = create_list_Executions(10)

    x = Group(27, "Group 0", "Speed")
    z = Group(28, "Group 1", "Speed")

    print z.get_executions()
    print x.get_executions()

    group_g1 = []
    group_g0 = []
    for each in list_executions:
        group_choice = each.get_index_metrics(0)
        g0 = 0
        g1 = 1

        if (group_choice == g0):
            print "g0"
            group_g0.append(each.get_id())
        if (group_choice == g1):
            print "g1"
            group_g1.append(each.get_id())
    z.add_execution(group_g0)
    x.add_execution(group_g1)

    # groups:
    print z.get_executions()
    print x.get_executions()

    return [x,z]


"Cross validation"
def cross(list_metrics):

    temp = []
    i = 0
    total = []
    for each in list_metrics:
        qtd = each.get_qtd_groups()
        list_ids = each.get_all_executions_by_group_index(i)
        total.append(list_ids)

    print set(total[0]).intersection(total[1])
    print set(total[1]).intersection(total[2])

    print "total"
    print total

"Main function"
def main():
    list = create_list_Executions(10)
    list_metrics = []
    # Metrics:
    m1 = Metric("Velocidade")
    m1.create_from_execution_list(list, 0, False)
    list_metrics.append(m1)
    print m1.get_executions_groups()

    m2 = Metric("Potencia")
    m2.create_from_execution_list(list, 1, False)
    list_metrics.append(m2)
    print m2.get_executions_groups()

    m3 = Metric("Camisa")
    m3.create_from_execution_list(list, 2, False)
    list_metrics.append(m3)
    print m3.get_executions_groups()

    #m1.create_groups([1,1,1,2,2,2,3,3,3,1,1])


    cross(list_metrics)
    # m2.show()
    # m3.show()

main()