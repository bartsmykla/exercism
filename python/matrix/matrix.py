class Matrix:
    def __init__(self, matrix_string):
        self._rows = [[int(n) for n in row.split(" ")] for row in matrix_string.split("\n")]
        self._columns = [list(row) for row in zip(*self._rows)]

    def row(self, index):
        return self._rows[index - 1]

    def column(self, index):
        return self._columns[index - 1]
