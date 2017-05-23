# import sys
# import babeltrace
# sys.path.append("/usr/local/lib/python%d.%d/site-packages")
#
# # get the trace path from the first command line argument
# trace_path = sys.argv[1]
#
# trace_collection = babeltrace.reader.TraceCollection()
#
# trace_collection.add_trace(trace_path, 'ctf')
#
# for event in trace_collection.events:
#     print(event.name)

from node import Node

#Reading File
def reading_file(file_name, Flag = False):
    "function_docstring"
    file_ = "/home/francisco/Downloads/traceAnalyze/case1/tracing_output.txt"
    with open(file_name, "r") as ins:
        array = []
        for line in ins:
            array.append(line)

    if(Flag):
        for each in array:
            print (each)

    return array

#Creating tree with repetition:
def create_tree(data, flag= False):
    entry = "lttng_ust_cyg_profile:func_entry"
    exit = "lttng_ust_cyg_profile:func_exit"

    tree = Node("root",[])
    pointer = tree

    metric1 = "perf_thread_page_fault"
    metric2 = "perf_thread_instructions"
    metric3 = "perf_thread_cache_misses"

    for each in data:
        if entry in each:
            begin = (each.find("addr"))
            begin += 7
            end = begin + 8
            name = (each[begin:end])
            if (flag):
                print ("cria no "+ name)
            if (metric1 in each):
                print (metric1)
                begin_m = (each.find(metric1))
                begin_m = begin_m + 25
                end_m =  begin_m + 1
                print (each[begin_m:end_m])

            aux = Node(name, [])
            pointer.add_child(aux)
            aux.set_parent(pointer)
            pointer = aux

        if exit in each:
            begin = (each.find("addr"))
            begin += 7
            end = begin + 8
            name = (each[begin:end])
            if (flag):
                print ("fecha no" + name)
            pointer = pointer.get_parent()

    return pointer

#Creating tree without repetition:
def create_cct(data, flag):
    entry = "lttng_ust_cyg_profile:func_entry"
    exit = "lttng_ust_cyg_profile:func_exit"

    tree = Node("root",[])
    pointer = tree

    for each in data:
        if entry in each:
            if (flag):
                print ("cria no")
            begin = (each.find("addr"))
            begin += 7
            end = begin + 7
            name = (each[begin:end])
            print (name)
            print ()
            if("perf_thread_page_fault" in each):
                print ("page faults")
            if(pointer.get_label() == name):
                if (flag):
                    print("already there")
                pointer.increment()
            else:
                aux = Node(name, [])
                pointer.add_child(aux)
                aux.set_parent(pointer)
                pointer = aux

        if exit in each:
            if(flag):
                print ("fecha no")
            pointer = pointer.get_parent()

    return tree

#inorder traversal:
def get_data(tree):
    list = tree.get_children()
    print (tree.get_label())

    i = 0
    while i < len(list):
        get_data(list[i])
        i = i + 1
    # for each in range(tree.get_children()):
    #   print(each.get_label())
    #   get_data(each.get_children())


  #Finding patterns
def finding_string(data, string):
    i = 0
    for each in range(data):
        i = i + 1
        if string in each:
            print (i)

