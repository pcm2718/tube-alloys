from matrix import Matrix, NullMatrix, IdentityMatrix

# Test script.

print "Null Matrix Test:"
print ""
nullmat = NullMatrix(4)
print nullmat
print ""
print ""


print "Identity Matrix Test:"
print ""
idmat = IdentityMatrix(5)
print idmat


print "Nontrival Matrix Test:"
print ""
print "mat ="
mat = Matrix(3, 3, [1, 2, 3, 2, 1, 3, 3, 2, 1])
print mat
print ""
print ""


print "Matrix Addition Test:"
print ""
print "mat1 ="
mat1 = Matrix(3, 2, [1, 2, 3, 2, 1, 3])
print mat1
print ""
print "mat2 ="
mat2 = Matrix(3, 2, [3, 2, 1, 3, 3, 2])
print mat2
print ""
print "mat1 + mat2 ="
print mat1 + mat2
print ""
print ""


print "Scalar Multiplication Test:"
print ""
print "mat * 3.7 ="
print mat * 3.7
print ""
print "3.7 * mat ="
print 3.7 * mat
print ""
print ""


print "Matrix Multiplication Test:"
print ""
print "mat1 ="
mat1 = Matrix(3, 2, [1, 2, 3, 2, 1, 3])
print mat1
print ""
print "mat2 ="
mat2 = Matrix(2, 3, [3, 2, 1, 3, 3, 2])
print mat2
print ""
print "mat1 * mat2 ="
print mat1 * mat2
print ""
print "mat2 * mat1 ="
print mat2 * mat1
print ""
print ""


print "Matrix Transpose Test"
print ""
print "mat1 ="
print mat1
print ""
print "mat1^t ="
print mat1.transpose()
print ""
print ""
