
from execution import Execution
from csv_module import *

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

    def get_name(self):
        return self.name

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

        "list_executions accumulates the executions by ids"
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

    "This function takes a list of executions and compares with its own group"
    def compare_metric(self, metric, flag, save = ""):

        id = 0
        set_b1 = self.get_executions_groups()
        set_b2 = metric.get_executions_groups()
        qtd = 1
        if(flag):
            print "Compare"
            print set_b1
            print set_b2

        list_result = []
        for eachB1 in set_b1:
            for eachB2 in set_b2:
                result = len(set(eachB1).intersection(eachB2))
                result = float(result)*100 / float(len(eachB1))
                list_result.append(result)
                if (flag):
                    print str(eachB1) + " " + str(eachB2) + " " + str(result)


        #metric1 groupx groupy metric2 percentage
        i = 0
        k = 0
        print_result = []
        for eachB1 in set_b1:
            j = 0
            for eachB2 in set_b2:
                if (flag):
                    print_result.append([self.get_name(), "g"+ str(i), "g" + str(j), metric.get_name(),str(list_result[k])])
                    print self.get_name() + ": g"+ str(i) +" g" + str(j) + " "+  metric.get_name() + " result = " + str(list_result[k])
                j = j + 1
                k = k + 1
            i = i + 1

        if(save == "save"):
            csv_write_list("results/percentage.csv", print_result, True)

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
                print "g1 " + str(b1) + " g2 " +  str(b2) + " " + str(result)
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

"This function creates a metric"
def create_metric(name, list, index, flag):

    m1 = Metric(name)
    m1.create_from_execution_list(list, index, flag)
    print name
    print m1.get_groups()

    return m1

"This function creates the metrics from the executions"
def create_list_metrics(list, max, flag):
    list_metrics = []

    str_name = "metric "

    i = 0
    while i < max:
        m = create_metric(str_name+ str(i), list, i,flag)
        list_metrics.append(m)
        i = i + 1

    return list_metrics

"Function to read csv file"
def read_csv_create_executions(path, flag):
    list_executions = csv_read_full(path)
    if(flag):
        print list_executions

    list_objects = []
    i = 0
    for each in list_executions:
        x = Execution(i, each)
        list_objects.append(x)
        i = i + 1

    return list_objects

"This function does the cross comparison of the groups vs metrics"
def cross_metrics(list_metrics):

    i = 0
    while i < len(list_metrics):
        j = 0
        temp = []
        m1 = list_metrics[i]
        while j < len(list_metrics):
            m2 = list_metrics[j]
            if (i != j):
                m1.compare_metric(m2, True, "save")
            j = j + 1
        i = i + 1

"Main function"
def main():
    #list = create_list_Executions(10)
    list = read_csv_create_executions("testsFiles/executions.csv", False) #("testsFiles/executions.csv", False)
    list_metrics = create_list_metrics(list, 3, False) #(list, 6)

    cross_metrics(list_metrics)
    # m1= list_metrics[0]
    # m2 = list_metrics[1]
    # m3 = list_metrics[2]
    # m1.compare_metric(m3, False,"save")

    #print "Cross validation"
    #total = take_all_groups(list_metrics)
    #print cross(total, 11, True)


main()
#read_csv_create_executions(False)