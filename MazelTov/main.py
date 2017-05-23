"This is the main file, responsible for controlling the behavior of system as a whole: reader, analysis and node"

from reader import *
from analysis import *

"Experiment"
def main():
    #read the file
    data = reading_file("/home/francisco/Downloads/traceAnalyze/case1/output_tracing.txt")

    #create the tree
    tree = create_tree(data, True)

    #create the analysis
    ana = Analysis(tree)
    content = []
    ana.traversal(content)
    print (content)

main()