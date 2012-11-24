
# For running matmult pthread evals.

FILE=pthread

echo "N=$1" >> results/matmult/$FILE
libdeterm/eval/exe/matmult >> results/matmult/$FILE

