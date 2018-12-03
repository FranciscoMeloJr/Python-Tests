def validate(words):
    """
    Compare the words in the list and return the new string list.
    :param words: list of words
    :return: new list of words without repetition, i.e. toto == ttoo.
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
            # 2:[cra] - car
            for each in list_values:
                if set(each) != set(each_word):
                    list_values.append(each_word)
                    result[key] = list_values

    #list comprehension for final list:
    return [result.get(each_key)[0] for each_key in result.keys()]


def test_assertions():
    """
    Do the assertions.
    """
    #validate:
    assert validate(['ttoo','toto','xt']) == ['toto', 'xt']
    assert validate(['ttoo','toto']) == ['toto']
    assert validate(['xt','tx']) == ['tx']
    assert validate(['xyt','xty','ytx']) == ['xty']
    assert validate(['']) == ['']

test_assertions()
