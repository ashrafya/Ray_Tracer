class matrix:
    def __init__(self, rows, cols, data):
        if rows != len(data):
            raise ValueError('rows does not have proper number of rows')
        for x in range(len(data)):
            if cols != len(data[x]):
                raise ValueError('incorrect number of columns for in row number {}'.format(x+1))
        self.rows = rows
        self.cols = cols
        self.data = data

    def __str__(self):
        """
        string representation of the matrix
        """
        return '\n'.join(list(map(str, self.data)))

    def __eq__(self, other):
        """
        checks if teh two matrices are equal, in terms of each element they have as well
        """
        if len(self.data) != len(other.data):
            return False
        for i in range(len(other.data)):
            if len(self.data[i]) != len(other.data[i]):
                return False

            for j in range(len(other.data[i])):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __mul__(self, other):
        final = []
        iteration = self.cols
        for row in range(self.rows):
            inner = []
            for col in range(other.cols):
                total=0
                for num in range(iteration):
                    total +=self.data[row][num] * other.data[num][col]
                inner.append(total)
            final.append(inner)
            inner = []
        return matrix(len(final), len(final[0]), final)

    def multiply_tuple(self, tuple):
        final = ()
        for i in range(self.rows):
            total = 0
            for j in range(len(tuple)):
                total += self.data[i][j]
            if i == len(tuple):
                return final
            final += total,
        return final

    def transpose(self):
        """
        transposes the matrix, which is basically switching the rows and columns in teh matrix
        """
        final = []
        for i in range(self.cols):
            final.append([])
        for row in range(self.rows):
            for col in range(self.cols):
                final[col].append(self.data[row][col])
        return final

    def determinant(self):
        """
        returns teh determinant of a matrix
        It can handle both matrix sizes of two by two and larger
        """
        det = 0
        if self.rows == 2 and self.cols == 2:
            det = self.data[0][0]*self.data[1][1] - self.data[1][0]*self.data[0][1]
        else:
            for i in range(self.cols):
                det += self.data[0][i] * self.cofactor(0, i)
        return det

    def submatrix(self, row, col):
        """
        removes the row and column specified, effectively scaling down the matrix size
        """
        og = []
        for i in range(self.rows):
            og.append([])

        for i in range(self.rows):
            for j in range(self.cols):
                og[i].append(self.data[i][j])

        # removes the row from the matrix
        og.remove(og[row])

        # remove the column
        for i in range(len(og)):
            og[i].pop(col)
        return matrix(len(og), len(og[0]), og)

    def minor(self, row, col):
        """
        return minor of the matrix at the specific row and col
        """
        return self.submatrix(row, col).determinant()

    def cofactor(self, row, col):
        """
        returns the cofactor of the at the specific row and col, a next step from minor at the row and column
        """
        if (row + col) % 2 == 1:
            return self.minor(row, col) * -1
        return self.minor(row, col)

    def invertible(self):
        """
        checks if the matrix is invertible or not
        the matrix is not invertible if teh determinant is equal to zero (0)
        """
        if self.determinant() == 0:
            return False
        return True

    def inverse(self):
        """
        returns the inverse matrix
        """
        # check if matrix is invertible or not
        if self.invertible() == 0:
            raise ValueError("matrix cannot be inverted")

        # make a new matrix with same data, but avoid aliasing which is a sometimes pitfall in python
        og = []
        for i in range(self.rows):
            og.append([])

        for i in range(self.rows):
            for j in range(self.cols):
                og[i].append(self.data[i][j])

        # check if it is a square matrix
        if self.rows != self.cols:
            raise ValueError("this is not a square matrix")

        # implement the algorithm to find the inverse
        for row in range(self.rows):
            for col in range(self.cols):
                c = self.cofactor(row, col)
                og[col][row] = c/self.determinant()
        return matrix(len(og), len(og[0]), og)


identity_matrix = matrix(4, 4, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])


if __name__ == '__main__':
    """
    these are all the tests used to check the functionality of teh functions
    they can be uncommented to play around with
    the gibberish line below has been added so that no errors show because the name == main function is empty
    """
    kjnasfflnasfnlsa = 1
    # A = [[1, 1, 1, 1], [2, 2, 2, 2]]
    # B = [[2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2]]
    # mat_A = matrix(2, 4, A)
    # mat_B = matrix(4, 3, B)
    # print(mat_A)
    # print(mat_B)
    # mat_C = mat_A * mat_B
    # print(mat_C)
    # big = [[1, 2, 3, 4], [2, 4, 4, 2], [8, 6, 4, 1], [0, 0, 0, 1]]
    # big = matrix(4, 4, big)
    # small = (1, 2, 3)
    # zero = big.multiply_tuple(small)
    # print(zero)
    # x = matrix(2, 2, ([[1, 5], [-3, 2]]))
    # print(x.determinant())
    # print()
    # sub = mat_A.submatrix(0, 2)
    # print(sub.rows, sub.cols, sub.data)
    # print(identity_matrix)
    # print(A)
    # print(mat_A.transpose())
    # P = matrix(3, 3, ([[3, 5, 0], [2, -1, -7], [6, -1, 5]]))
    # print(P.minor(0, 0))
    # print(P.cofactor(0, 0))
    # print(P.minor(1, 0))
    # print(P.cofactor(1, 0))
    # M = matrix(3, 3, ([[1, 2, 6], [-5, 8, -4], [2, 6, 4]]))
    # N = matrix(4, 4, ([[-2, -8, 3, 5], [-3, 1, 7, 3], [1, 2, -9, 6], [-6, 7, 7, -9]]))
    # print(M.determinant(), M.invertible())
    # print(N.determinant(), N.invertible())
    # M.inverse()
    # Z = matrix(4,4,([[-5, 2, 6, -8], [1, -5, 1, 8], [7, 7, -6, -7], [1, -3, 7, 4]]))
    # print(Z.inverse())
    # print()
    # Q = matrix(4, 4, ([[8, -5, 9, 2], [7, 5, 6, 1], [-6, 0, 9, 6], [-3, 0, -9, -4]]))
    # print(Q.inverse())
    # print()
    # wow = matrix(4, 4, ([[9, 3, 0, 9], [-5, -2, -6, -3], [-4, 9, 6, 4], [-7, 6, 6, 2]]))
    # print(wow.inverse())
    # print()
    # one = matrix(4, 4, ([[3, -9, 7, 3], [3, -8, 2, -9], [-4, 4, 4, 1], [-6, 5, -1, 1]]))
    # two = matrix(4, 4, ([[8, 2, 2, 2], [3, -1, 7, 0], [7, 0, 5, 4], [6, -2, 0, 5]]))
    # three = one * two
    # # print(three)
    # inv_two = two.inverse()
    # print((three * inv_two))
