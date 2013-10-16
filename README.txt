src/matrixtest.py can be run to ensure that all numerical operations in the Matrix
class are working properly. You probably shouldn't need to do this:
	python matrixtest.py

src/choleskydemo.py is a noninteractive demo demonstrating LL^t and LDL^t
decomposition using the code from Tube Alloys.
	python choleskydemo.py

src/interpreter.py is a script to be run before starting the Python interpeter,
preparing it for interactive use.
	python -i interpreter.py

interpreter.sh is a bash script for use on UNIX systems, it simply runs the
command above from the root directory.

src/matrix.py is a code file containing a class describing a basic Matrix class,
as well as the utility subclasses NullMatrix and IdentityMatrix.

src/cholesky.py contains the actual code for Cholesky decompositions.
