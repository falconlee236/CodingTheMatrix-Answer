# Copyright 2013 Philip N. Klein
from vec import Vec
# Test your Mat class over R and also over GF(2).
# The following tests use only R.


def getitem(M, k):
    """
    Returns the value of entry k in M, where k is a 2-tuple
    """
    assert k[0] in M.D[0] and k[1] in M.D[1]
    return M.f[(k[0], k[1])] if k in M.f.keys() else 0


def equal(A, B):
    """
    Returns true iff A is equal to B.

    Consider using brackets notation A[...] and B[...] in your procedure
    to access entries of the input matrices.  This avoids some sparsity bugs.
    """
    assert A.D == B.D
    for key in A.f:
        if A[key] != B[key]:
            return False
    for key in B.f:
        if A[key] != B[key]:
            return False
    return True


def setitem(M, k, val):
    """
    Set entry k of Mat M to val, where k is a 2-tuple.
    """
    assert k[0] in M.D[0] and k[1] in M.D[1]
    M.f[(k[0], k[1])] = val


def add(A, B):
    """
    Return the sum of Mats A and B.

    Consider using brackets notation A[...] or B[...] in your procedure
    to access entries of the input matrices.  This avoids some sparsity bugs.
    """
    assert A.D == B.D
    m = Mat(A.D, {})
    for key, value in A.f.items():
        m[key] += value
    for key, value in B.f.items():
        m[key] += value
    return m


def scalar_mul(M, x):
    """
    Returns the result of scaling M by x.

    """
    return Mat(M.D, {key: value*x for key, value in M.f.items()})


def transpose(M):
    """
    Returns the matrix that is the transpose of M.
    """
    return Mat((M.D[1], M.D[0]), {(key[1], key[0]): value for key, value in M.f.items()})


def vector_matrix_mul(v, M):
    """
    returns the product of vector v and matrix M

    Consider using brackets notation v[...] in your procedure
    to access entries of the input vector.  This avoids some sparsity bugs.

    
    """
    assert M.D[0] == v.D
    res = {k: 0 for k in M.D[1]}
    for i, j in M.f:
        res[j] += (M[i, j] * v[i])
    return Vec(M.D[1], res)


def matrix_vector_mul(M, v):
    """
    Returns the product of matrix M and vector v.

    Consider using brackets notation v[...] in your procedure
    to access entries of the input vector.  This avoids some sparsity bugs.

    
    """
    assert M.D[1] == v.D
    res = {k: 0 for k in M.D[0]}
    for i, j in M.f:
        res[i] += (M[i, j] * v[j])
    return Vec(M.D[0], res)


def matrix_matrix_mul(A, B):
    """
    Returns the result of the matrix-matrix multiplication, A*B.

    Consider using brackets notation A[...] and B[...] in your procedure
    to access entries of the input matrices.  This avoids some sparsity bugs.

    """
    assert A.D[1] == B.D[0]
    res = {(i[0], j[1]): 0 for i in A.f for j in B.f}
    for i, j in A.f:
        for x, y in B.f:
            if j == x:
                res[i, y] += (A[i, j] * B[x, y])
    return Mat((A.D[0], B.D[1]), res)
###############################################################################


class Mat:
    def __init__(self, labels, function):
        assert isinstance(labels, tuple)
        assert isinstance(labels[0], set) and isinstance(labels[1], set)
        assert isinstance(function, dict)
        self.D = labels
        self.f = function

    __getitem__ = getitem
    __setitem__ = setitem
    transpose = transpose

    def __neg__(self):
        return (-1)*self

    def __mul__(self, other):
        if Mat == type(other):
            return matrix_matrix_mul(self, other)
        elif Vec == type(other):
            return matrix_vector_mul(self, other)
        else:
            return scalar_mul(self, other)
            # this will only be used if other is scalar (or not-supported).
            # mat and vec both have __mul__ implemented

    def __rmul__(self, other):
        if Vec == type(other):
            return vector_matrix_mul(other, self)
        else:  # Assume scalar
            return scalar_mul(self, other)

    __add__ = add

    def __radd__(self, other):
        "Hack to allow sum(...) to work with matrices"
        if other == 0:
            return self

    def __sub__(a, b):
        return a+(-b)

    __eq__ = equal

    def copy(self):
        return Mat(self.D, self.f.copy())

    def __str__(M, rows=None, cols=None):
        "string representation for print()"
        if rows is None:
            rows = sorted(M.D[0], key=repr)
        if cols is None:
            cols = sorted(M.D[1], key=repr)
        separator = ' | '
        numdec = 3
        pre = 1+max([len(str(r)) for r in rows])
        colw = {col: (1+max([len(str(col))] + [len('{0:.{1}G}'.format(M[row, col], numdec))
                                               if isinstance(M[row, col], int) or isinstance(M[row,col], float)
                                               else len(str(M[row, col])) for row in rows])) for col in cols}
        s1 = ' '*(1 + pre + len(separator))
        s2 = ''.join(['{0:>{1}}'.format(str(c), colw[c]) for c in cols])
        s3 = ' '*(pre+len(separator)) + '-'*(sum(list(colw.values())) + 1)
        s4 = ''.join(['{0:>{1}} {2}'.format(str(r), pre, separator)+''.join(['{0:>{1}.{2}G}'.format(M[r, c], colw[c], numdec)
                                                                             if isinstance(M[r, c], int) or isinstance(M[r, c], float)
                                                                             else '{0:>{1}}'.format(M[r, c], colw[c]) for c in cols])+'\n' for r in rows])
        return '\n' + s1 + s2 + '\n' + s3 + '\n' + s4

    def pp(self, rows, cols):
        print(self.__str__(rows, cols))

    def __repr__(self):
        "evaluatable representation"
        return "Mat(" + str(self.D) + ", " + str(self.f) + ")"

    def __iter__(self):
        raise TypeError('%r object is not iterable' % self.__class__.__name__)
