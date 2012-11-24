
# For running deterministic matmult evals.

FILE=det

echo "N=$1" >> results/matmult/$FILE
libdeterm/user/exe/matmult >> results/matmult/$FILE

