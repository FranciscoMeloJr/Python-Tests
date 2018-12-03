# Based on insertion search

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
    words = sorted(words, key=len)

    #Final result
    final = []
    # Get the size - create a dict: size:[word1,word2,word3]
    if len(words) < 1:
        return []
    final.append(words[0])

    flag = True
    for i in range(1, len(words)):
        flag = True
        for each in final:
            if len(words[i]) == len(each) and set(words[i]) == set(each):
                flag = False
        if flag:
            final.append(words[i])
    return final


def test_assertions():
    #validate:
    assert validate(['ttoo','toto','xt']) == ['toto', 'xt']
    assert validate(['ttoo','toto']) == ['toto']
    assert validate(['ttoo','oott','toto']) == ['oott']
    #size 2:
    assert validate(['xt', 'tx']) == ['tx']
    assert validate(['xt', 'tx', 'xx']) == ['tx', 'xx']
    #empty
    assert validate([]) == []


test_assertions()