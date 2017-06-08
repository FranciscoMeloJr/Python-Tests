"This is the Decision Tree Classification algorithm"

class Pet(object):

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)

class Execution(object):

   def get_metric0(self):
       return self.metric_list[0]

   def get_metric1(self):
       return self.metric_list[1]

   def get_metric2(self):
       return self.metric_list[2]

   def get_metric_n(self, n):
       return self.metric_list[n]

   def __init__(self, list_1):
       self.metric_list = list_1


"Experiment"
def create_executions():
    list_total = []
    mini_list = [1,1,0]
    x = Execution(mini_list)
    y = Execution([0, 0, 0])
    z = Execution([1, 0, 1])

    i = 0
    while i < 10:
        list_total.append(x)
        i +=1

    i = 0
    while i < 10:
         list_total.append(y)
         i += 1

    i = 0
    while i < 10:
         list_total.append(z)
         i += 1

    return list_total

"Get list of metric"
def get_list_metrics(list_exe, index):

    list_total = []
    for each in list_exe:
        list_total.append(each.get_metric_n(index))
    return list_total

"Compare two list in terms of percentage"
def compare_lists(list_1, list_2):

    percentage_compare = 0
    i = 0
    while i < len(list_1):
        if(list_1[i] == list_2[i]):
            percentage_compare +=1
        i +=1

    return float(float(percentage_compare)/len(list_1)*100)


"Experiment"
def main():
    list_exe = create_executions()
    list_metric0= get_list_metrics(list_exe, 0)
    print(compare_lists([0,0,0,1,1],[1,1,1,1,1]))

main()