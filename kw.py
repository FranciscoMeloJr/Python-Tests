#!/usr/bin/python
from scipy import stats
from scipy.stats import chi2
            
def test():
    x = [1, 1, 1]
    y = [2, 2, 2]
    z = [2, 2]
    result = stats.kruskal(x,y)
    print result

#kruskal willis:
def kruskal_willis(list_a, flag):
    
    vec = []
    list_sum = []
    df = len(list_a) - 1

        
    for each in list_a:
        if(flag):
            print each
        sum_ = 0
        i = 0
        for each_number in each:
            vec.append(each_number)
            sum_ += each_number

        
    #create rank:
    rank = sorted(vec)
    
    #new list with ranks:
    temp_total =[]
    for each in list_a:
        temp = []

        for each_item in each:
            i = 0
            temp.append(find_number(each_item, rank, flag))
        temp_total.append(temp)

    for each in temp_total:
        list_sum.append(calculate_total(each, flag))
        
    print "total:"
    print temp_total
    print "sum:"
    print list_sum
    
    if(flag):
        print rank
        print list_sum
        print df
        
    h = calculate_h(12, 18, list_sum, flag)
    #compare with qui square:
    p = 0.05
    df = len(list_a)-1
    ch_value =  chi2.isf(p, df)

    return evaluate_chi(ch_value, h)
    
#arrange repetitions:
def evaluate_chi(ch_value, h):
    if (h > ch_value):
        print "Reject H0"
        return True
    
    print "NOT Reject H0"
    return False
    

#arrange repetitions:
def find_number(number, rank, flag):
    i = 0
    result = []
    while i < len(rank):
        if(rank[i] == number):
            result.append(int(i+1))
        i+=1

    if(flag):
        print type(result)
    
    if (len(result) > 1):
        total = 0
        for each in result:
            total += each
        return total /  len(result)
    else:
        return result[0]
    
    
#calculate the total:
def calculate_total(list_x, flag):
    total = 0
    for each in list_x:
        total +=each

    if(flag):
            print total
    return total

#calculate the total:
def calculate_sum_sq(list_sum, n, flag):
    
    #for each in list:
    if(flag):
        print list_sum
    ret = 0
    for each in list_sum:
        ret += ((each*each)/n)

    print ret
    return ret

#count the repetitions:
def calculate_h(n, size, list_sum, flag):

    list_value = calculate_sum_sq(list_sum, 6, flag)

    if(flag):
        print list_value    
    #(12 /( 18(18+1))) * (43^2/6 + 61^2/6 + 67^2/6) -3(18+1)
    ret =  (float (12/float ((18*(18+1))))) * (list_value) - (3*(18+1))

    if(flag):
        print ret
        
    return ret
    
#count the repetitions:
def count_repetitions():
    print "oi"
    
test_list = [[8.2,10.3,9.1,12.6,11.4,13.2],[10.2,9.1,13.9,14.5,9.1,16.4],[13.5,8.4,9.6,13.8,17.4,15.3]]    
print kruskal_willis(test_list, False)

