Read in data from 2 input files named �project1_part3a.txt� & �project1_part3b.txt� found in the
project section on Blackboard. Column 1 contains the required data in both files.! !
Read the data from both files into matrices, A & B.! !
****** Note the change to the row and col from the original post ***********!
A should be a 1,000 x 10,000 matrix, B should be a 10,000 x 1,000 matrix.! !
Generate the resulting matrix multiplication of A & B in parallel as follows:! !
Using mpi4py, break the row-column multiply & sum operations into 10 iterations by using all the
rows in A times the first 1000 columns of B, then the rows of A times the next 1000 columns of
B, etc. until all the columns of B have been used. Distribute each iteration to a separate process
for calculation in a slave node (you should be using 10 total processes). Return the resulting
sub-matrix of each process back to the master node for reassembly into the final matrix answer.
Write the final matrix to a text file in the home directory as a file named �project1_part3final.txt�.!