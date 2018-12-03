
def create_new_list(list_values):
    #['ot', 'to', 'tt']
    #['to', 'tt']
    sorted(list_values)

    list_new = [list_values[0]]
    flag = True
    for i in range(1, len(list_values)):
        flag = True
        for each in list_new:
            if set(list_values[i]) == set(each):
                flag = False
        if flag:
            list_new.append(list_values[i])
    return list_new

def test():
    """
    Test the words on the list
    """
    string_a = 'toto'
    string_b = 'ttoo'
    string_c = 'tt'
    string_d = 'to'
    string_e = 'ot'
    string_f = 'ttt'

    list_a = [string_c, string_c, string_a, string_b, string_d, string_e, string_f]
    exp = ['toto']


def validate(words):
    """
    Compare the words in the list.
    :param words: list of words
    :return: new list of words.
    """
    result = {}
    # Eliminate duplicate words:
    words = list(set(words))
    # Order:
    words = sorted(words)

    #Final result
    final = []
    # Get the size - create a dict: size:[word1,word2,word3]
    for each_word in words:
        key = len(each_word)
        if key not in result:
            result[key] = [each_word]
        else:
            list_values = result[key]
            list_values.append(each_word)
            result[key] = list_values

    #organizing the list of keys:
    list_keys = result.keys()
    list_keys = sorted(list_keys)

    for each_key in list_keys:
        list_values = result.get(each_key)
        s = create_new_list(list_values)
        final.extend(s)
    return final

def test_assertions():
    #test new list:
    assert create_new_list(['yt', 'ty','to']) == ['yt', 'to']
    assert create_new_list(['yxt', 'xyt','tyx']) == ['yxt']
    assert create_new_list(['yxt', 'xyt']) == ['yxt']
    assert create_new_list(['yt', 'ty','tt']) == ['yt', 'tt']

    #validate:
    assert validate(['ttoo','toto','xt']) == ['xt', 'toto']
    assert validate(['ttoo','toto']) == ['toto']
    assert validate(['xt','tx']) == ['tx']
    assert validate(['xyt','xty','ytx']) == ['xty']

def test_sets():
    list_a = ['toto','ttoo','tt']
    s = list(set(list_a))
    print("First test", s)

    list_b = ['t','toto','tt','to','ot']
    s1 = set(list_b)
    sorted(s1)
    if 'to' not in s1:
        s1.add('tt')

    print("Second test", s1)
