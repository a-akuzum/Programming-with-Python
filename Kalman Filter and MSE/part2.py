
#................PROJECT1 / PART 2 .......................

import numpy
import scipy.signal
from pylab import *
import matplotlib.pyplot
from matplotlib.backends.backend_pdf import PdfPages

#Read Input
f = numpy.loadtxt('project1_part2.txt')

#Weiner Filter
weiner_filter = scipy.signal.wiener(f[0:999],3,1.0)

#Calculate MSE
x = 0;
for i in range(999):
    x = x + (f[i]-weiner_filter[i])**2
mse = x/999


#Ploting
a=matplotlib.pyplot.figure()
matplotlib.pyplot.plot(f,'b')
matplotlib.pyplot.plot(weiner_filter,'r')
matplotlib.pyplot.title('Mean Square Error')
text(60, 70, "MSE=%.4f" %mse);
legend(['Input','Predicted']);
show()

#Save as a PDF Format
Pdf=PdfPages('Plot.pdf')
Pdf.savefig(a)
Pdf.close()

#Creating output text file and write datas
results=open("project1_part2final.txt",'w')
results.write('  ORIGINAL'+'\t\t'+'  PREDICTED'+'\t\t'+'  ERROR'+'\n\n')
for k in range(1,999):
    results.write(str(f[k])+'\t\t'+str(weiner_filter[k-1])+'\t\t'+str((f[k]-weiner_filter[k-1]))+'\n');

results.close()


