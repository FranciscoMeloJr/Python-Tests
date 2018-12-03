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
    words = sorted(words)

    #Final result
    final = []
    # Get the size - create a dict: size:[word1,word2,word3]
    if len(words) < 1:
        return []
    final.append(words[0])

    #number_list = [ x for x in range(20) if x % 2 == 0]

    final = [words[0]]
    final = [ words[i] for i in range(1, len(words)) for j in range(0, len(final)) if len(words[i]) == len(final[j]) if set(words[i]) != set(final[j])]

    print(final)
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