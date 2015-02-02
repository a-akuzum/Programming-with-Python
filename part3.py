

#....................PROJECT1 / PART3....................


from mpi4py import MPI
import numpy

sendbuff=[]
root=0
comm=MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# READING FROM FILE
A1 = open ("project1_part3a.txt","r")
B1 = open ("project1_part3b.txt","r")

A2 = A1.readlines()
B2 = B1.readlines()

# CHANGING TO ARRAY FROM LIST
A_array = numpy.array(A2)
B_array = numpy.array(B2)

# SLICING DATA BECAUSE THERE IS ONE EXTRA DATA FOR MATRIX SIZE
A_slicing = A_array[:10000000]
B_slicing = B_array[:10000000]

# A MATRIX AND B MATRIX
Ashape = (1000, 10000)
Amat = A_slicing.reshape(Ashape)

Bshape = (10000, 1000)
Bmat = B_slicing.reshape(Bshape)

# CHANGING FROM STRING TO FLOAT
A = Amat.astype(numpy.float)
B = Bmat.astype(numpy.float)


yr=numpy.split(Bshape,size,axis=1)

if rank==0:
	yr=yr
v=comm.scatter(yr, root)


# TO CHANGE ROW A
total=[]
for j in range(1000):
	Arow1all=A[j,:]
	totalsum=[]
	
	# TO CHANGE COL B EACH TIME 1000 SHIFT (10 PROCESS TOTAL)
	for i in range(1000):
	
		def first1000():
			print "\n.......1000 of B[%d,%d] multiplaciation........" %(j,i)
			list2=[]
			for item in range (10000):
				list2.append(0)

			Bcol1all=B[:,i]
			list2[0:1001]=Bcol1all[0:1001]
			firstmul1=numpy.dot(Arow1all, list2)
			return firstmul1

		B = Bmat.astype(numpy.float)

		def second1000():
			list2=[]
			for item in range (10000):
				list2.append(0)

			Bcol2all=B[:,i]
			list2[1000:2001]=Bcol2all[1000:2001]
			firstmul2=numpy.dot(Arow1all, list2)
			return firstmul2

		B = Bmat.astype(numpy.float)

		def third1000():
			list2=[]
			for item in range (10000):
				list2.append(0)
	
			Bcol3all=B[:,i]
			list2[2000:3001]=Bcol3all[2000:3001]
			firstmul3=numpy.dot(Arow1all, list2)
			return firstmul3
	
		B = Bmat.astype(numpy.float)
	
		def fourth1000():
			list2=[]
			for item in range (10000):
				list2.append(0)
	
			Bcol4all=B[:,i]
			list2[3000:4001]=Bcol4all[3000:4001]
			firstmul4=numpy.dot(Arow1all, list2)
			return firstmul4
	
		B = Bmat.astype(numpy.float)
	
		def fifth1000():
			list2=[]
			for item in range (10000):
				list2.append(0)
		
			Bcol5all=B[:,i]
			list2[4000:5001]=Bcol5all[4000:5001]
			firstmul5=numpy.dot(Arow1all, list2)
			return firstmul5
	
		B = Bmat.astype(numpy.float)
	
		def sixth1000():
			list2=[]
			for item in range (10000):
				list2.append(0)
	
			Bcol6all=B[:,i]
			list2[5000:6001]=Bcol6all[5000:6001]
			firstmul6=numpy.dot(Arow1all, list2)
			return firstmul6
	
		B = Bmat.astype(numpy.float)
	
		def seventh1000():
			list2=[]
			for item in range (10000):
				list2.append(0)
	
			Bcol7all=B[:,i]
			list2[6000:7001]=Bcol7all[6000:7001]
			firstmul7=numpy.dot(Arow1all, list2)
			return firstmul7
	
		B = Bmat.astype(numpy.float)
	
		def eigth1000():
			list2=[]
			for item in range (10000):
				list2.append(0)
		
			Bcol8all=B[:,i]
			list2[7000:8001]=Bcol8all[7000:8001]
			firstmul8=numpy.dot(Arow1all, list2)
			return firstmul8
	
		B = Bmat.astype(numpy.float)
	
		def nineth1000():
			list2=[]
			for item in range (10000):
				list2.append(0)
	
			Bcol9all=B[:,i]
			list2[8000:9001]=Bcol9all[8000:9001]
			firstmul9=numpy.dot(Arow1all, list2)
			return firstmul9
	
		B = Bmat.astype(numpy.float)
	
		def tenth1000():
			list2=[]
			for item in range (10000):
				list2.append(0)
	
			Bcol10all=B[:,i]
			list2[9000:10001]=Bcol10all[9000:10001]
			firstmul10=numpy.dot(Arow1all, list2)
			return firstmul10
	
		def totalcolsum():
			sumoffirstcolofB= first1000()+second1000()+third1000()+fourth1000()+fifth1000()+sixth1000()+seventh1000()+eigth1000()+nineth1000()+tenth1000()
			totalsum.append(sumoffirstcolofB)
			
			# TO CREATE AND WRITE DATA FOR EACH SUB-MATRIX
			final = open('project1_part3final.txt','a') 
			old_stdout = sys.stdout  
			sys.stdout = final  
			
			print "--------------------------------"			
			print sumoffirstcolofB,"=Sum of coloumn B[%d,%d] matrix" %(j,i)
			print "--------------------------------"			
						
			sys.stdout=old_stdout 
			print 'Sub-Matrix \n' 
			
			return totalsum
			final.close() 
		print totalcolsum()

print "Rank %d scattered " % rank + str(v.shape)

if comm.rank == 0:
	final = numpy.concatenate ((recvbuff[:size]), axis=1)
	print final
	output = open('project1_part3final.txt','w')
	output.write(str(final))
	output.close




















