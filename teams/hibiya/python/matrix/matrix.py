class Matrix:
    def __init__(self, matrix_string):
        self.arr = []
        for row in matrix_string.split('\n'):
            self.arr.append([])
            for col in row.split():
                self.arr[-1].append(int(col))

    def row(self, index):
        return self.arr[index-1]

    def column(self, index):
        rtv = []
        for row in self.arr:
            rtv.append(row[index-1])
        return rtv