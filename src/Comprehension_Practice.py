def dictlist_helper(dlist, k):
    return [d[k] for d in dlist]


print(dictlist_helper([{'a': 'apple', 'b': 'bear'}, {'a': 1, 'b': 2}], 'a'))