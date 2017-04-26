class Matrix(object):
    '''This class represents matrices.'''

    def __init__(self, data):
        self._data = data

    def _getData(self):
        return self._data


    # getitem and setitem are for overloading the square bracket operator []
    def __getitem__(self, pos):
        if isinstance(pos, tuple):
            x, y = pos
            return self._data[x][y]
        else:
            return self._data[pos]

    def __setitem__(self, pos, value):
        x, y = pos
        self._data[x][y] = value

    data = property(_getData)

    
    @staticmethod
    def filled(rows=1, cols=1, value=0):
        twoD_lst = [[value for x in range(cols)] for y in range(rows)]
        obj = Matrix(twoD_lst)
        return obj


    def __len__(self):
        return len(self._data)


    def __str__(self):
        out = '\n'.join(str(elem) for elem in self._data)
        return '[' + out + ']'


    @property
    def T(self):
        n_rows = len(self._data)
        n_cols = len(self._data[0])
        transpose = Matrix.filled(rows=n_rows, cols=n_cols, value=0)
        for i in range(n_rows):
            for j in range(n_cols):
               transpose[j][i] = self._data[i][j]
        return transpose


    def __add__(self, other):
        n_rows = len(self._data)
        n_cols = len(self._data[0])
        c = Matrix.filled(rows=n_rows, cols=n_cols, value=0)
        for i in range(n_rows):
            for j in range(n_cols):
                c[i,j] = self._data[i][j] + other[i,j]
        return c


    # left multiplication
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            n_rows = len(self._data)
            n_cols = len(self._data[0])
            # create result Matrix
            c = Matrix.filled(rows=n_rows, cols=n_cols, value=0)
            for i in range(n_rows):
                for j in range(n_cols):
                    c[i,j] = self._data[i][j] * other
            return c
        else:
            first_matrix_rows = len(self._data)
            second_matrix_cols = len(other[0])
            # create result Matrix
            c = Matrix.filled(rows=first_matrix_rows, cols=second_matrix_cols, value=0)
            for i in range(first_matrix_rows):
                for j in range(second_matrix_cols):
                    for k in range(len(other)):
                        c[i,j] += self._data[i][k] * other[k,j]
            return c


    # right multiplication
    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            n_rows = len(self._data)
            n_cols = len(self._data[0])
            # create result Matrix
            c = Matrix.filled(rows=n_rows, cols=n_cols, value=0)
            for i in range(n_rows):
                for j in range(n_cols):
                    c[i,j] = self._data[i][j] * other
            return c
