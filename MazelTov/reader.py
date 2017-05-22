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
def reading_file():
    "function_docstring"
    with open("/home/francisco/Downloads/traceAnalyze/case1/tracing_output.txt", "r") as ins:
        array = []
        for line in ins:
            array.append(line)

    for each in array:
        print (each)

    return array

#Reading File
def create_tree(data):
    entry = "lttng_ust_cyg_profile:func_entry"
    exit = "lttng_ust_cyg_profile:func_exit"

    tree = Node(-1, ["root"])
    pointer = tree

    for each in data:
        if entry in each:
            print ("cria no")
            begin = (each.find("addr"))
            begin += 7
            end = begin + 7
            print (each[begin:end])
            aux = Node(-1, ["entry"])
            pointer.add_child(aux)
            aux.set_parent(pointer)
            pointer = aux

        if exit in each:
            print ("fecha no")
            pointer = pointer.get_parent()

#Finding patterns
def finding_string(data, string):
    i = 0
    for each in data:
        i = i + 1
        if string in each:
            print (i)




data = reading_file()
# finding_string(data, "lttng_ust_cyg_profile:func_entry")
# finding_string(data, "lttng_ust_cyg_profile:func_exit")
create_tree(data)