import math
import sys
from matrix import Matrix, NullMatrix, IdentityMatrix

class Cholesky:

    def __init__(self):
        pass



    def llt_decomp(self, matrix):
        if matrix.n != matrix.m or matrix.values != matrix.transpose().values:
            raise ValueError("Cannot decompose non-Hermitian matrix.")

        l = self.r_llt_decomp(0, matrix, IdentityMatrix(matrix.n))
        return {'L': l, 'L^t':l.transpose()}

    def r_llt_decomp(self, i, a_mat, l_mat):
        if i == a_mat.n:
            return l_mat

        # Get the scalar a_ii.
        a_sca = a_mat[i, i]
        # Get the vector b_i.
        b_vec = [0] * a_mat.n
        b_vec[i+1:a_mat.n] = a_mat.get_col(i)[i+1:a_mat.n]


        # Begin computing L_i+1.

        # Set up an identity matrix for the new term of L.
        m_mat = IdentityMatrix(a_mat.n)

        # Set M[i, i] to sqrt(a[i, i]).
        #print "a_sca:" + str(a_sca)
        m_mat[i, i] = math.sqrt(a_sca)

        # Set the term to a[i+1, i]/sqrt(a[i, i]).
        for k in range(i+1, a_mat.n):
            m_mat[k, i] = b_vec[k]/m_mat[i, i]

        # End computing L_i+1.


        # Begin computing A_i+1.

        # Set up the vectors b_i and b_i^t to compute the outer product op_mat.
        op_mat = Matrix(len(b_vec), 1, b_vec) * Matrix(1, len(b_vec), b_vec)

        b_mat = NullMatrix(a_mat.n)
        for p in range(i+1, a_mat.n):
            for q in range(i+1, a_mat.m):
                b_mat[p, q] = a_mat[p, q]

        c_mat = b_mat - (1/a_sca)*op_mat

        for k in range(0, i):
            c_mat[k, k] = 1

        # End computing A_i+1.


        return self.r_llt_decomp(i+1, c_mat, l_mat*m_mat)



    def ldlt_decomp(self, matrix):
        if matrix.n != matrix.m or matrix.values != matrix.transpose().values:
            raise ValueError("Cannot decompose non-Hermitian matrix.")

        l = self.llt_decomp(matrix)['L']
        d = IdentityMatrix(matrix.n)
       
        # This loop just factors out D from L and L^t.
        for i in range(0, d.n):
            d[i, i] = l[i, i]
            for j in range(i, d.n):
                l[j, i] = l[j, i]/d[i, i]
            d[i, i] = d[i, i] ** 2

        return {'L': l, 'D':d, 'L^t':l.transpose()}
