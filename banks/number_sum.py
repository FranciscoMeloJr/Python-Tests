
def sum_numbers(n,u):
    """
    This function sums the divirsos of one numbers.
    :return: All numbers that divide by the passed value
    """
    result = []
    below = 1
    upper = u
    for i in range(below, upper+1):
        if i % n == 0:
            result.append(i)

    return result

first = sum_numbers(13,1000)
second = sum_numbers(31,1000)

merged = first + second
#sort
merged.sort()
#set
exc_list = list(set(merged))
exc_list.sort()
print(exc_list)

#sum
print(sum(exc_list))