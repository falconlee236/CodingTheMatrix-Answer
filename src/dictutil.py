# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist): return [dct[i] for i in keylist]


def list2dict(L, keylist): return {key: value for key, value in zip(keylist, L)}
