#File to test the classes on this directory
from execution import Execution
from metric import *

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

test_create_executions()