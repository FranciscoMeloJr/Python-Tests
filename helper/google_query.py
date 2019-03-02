#Module for Google:
def do_query(query, print_flag=False, *, n_result = 10):
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")

    # to search
    #query = "Geeksforgeeks"

    for j in search(query, tld="com", num=n_result, stop=1, pause=2):
        if print_flag:
            print(j)

#Do multiple queries
def multiple_queries(total, print_flag):
    for each_issue in total:
        do_query(each_issue, print_flag)