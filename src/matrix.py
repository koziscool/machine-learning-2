



class Matrix:
    def __init__(self, elements):
        self.elements = elements
        self.num_rows = len(elements)
        self.num_cols = len(elements[0])

    def row(self, r):
        return self.elements[r]

    def col(self, c):
        ret_arr = []
        for i in range(self.num_rows):
            ret_arr.append(self.elements[i][c])
        return ret_arr
        
    def new_zero_matrix(self, num_rows, num_cols):
        M = []
        for i in range(num_rows):
            arr = []
            for j in range(num_cols):
                arr.append(0)
            M.append(arr)
        return Matrix(M)

    def copy(self):
        copied_elements = [[entry for entry in row] for row in self.elements]
        return Matrix(copied_elements)

    def add(self, M):
        if self.num_rows == M.num_rows and self.num_cols == M.num_cols:
            R = self.new_zero_matrix(self.num_rows, self.num_cols)
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    R.elements[i][j] = self.elements[i][j] + M.elements[i][j]
            return R
        
    def subtract(self, M):
        if self.num_rows == M.num_rows and self.num_cols == M.num_cols:
            R = self.new_zero_matrix(self.num_rows, self.num_cols)
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                   R.elements[i][j] = self.elements[i][j] - M.elements[i][j]
            return R

    def scalar_multiply(self, a):
        R = self.new_zero_matrix(self.num_rows, self.num_cols)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                   R.elements[i][j] = a * self.elements[i][j]
        return R