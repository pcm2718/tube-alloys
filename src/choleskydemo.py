from cholesky import Cholesky
from matrix import Matrix, NullMatrix, IdentityMatrix

decomp = Cholesky()
matrix = Matrix(3, 3, [4, 12, -16, 12, 37, -43, -16, -43, 98])
llt = decomp.llt_decomp(matrix)
ldlt = decomp.ldlt_decomp(matrix)

print ""
print ""
print "Test Matrix:"
print matrix
print ""
print ""
print "LL^t decomposition:"
print ""
print "L ="
print llt['L']
print "L^t ="
print llt['L^t']
print ""
print ""
print "LDL^t decomposition:"
print ""
print "L ="
print ldlt['L']
print "D ="
print ldlt['D']
print "L^t ="
print ldlt['L^t']
print ""
print ""
