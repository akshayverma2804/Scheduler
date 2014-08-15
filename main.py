from lib import pre_processorE,round_robin,priority_queue,graphxy,rr,pq
from random import randint

inFile = raw_input('Enter the file name : ');

inputFile = open(inFile, 'r')
text = inputFile.read()
lines = text.split('\n')
T = int(lines[0])

Towrite = ""
Towritepq = ""

for i in range(T):
        pre_processorE.allot_time(lines[i+1], i+1)
        #raw_input('Time allocated ......\nPress Enter to Continue..... ') 
        
        opfile = "Time/op"+str(i+1)+".txt"
        rfile = open(opfile, 'r')
        filecontent = rfile.read() 
        Times = filecontent.split('\n')
        miss = rr.setData(lines[i+1],i+1,Times)
        #print miss
        Towrite+=(lines[i+1]+" "+str(miss)+"\n")
        miss1 = rr.setData(lines[i+1],i+1,Times)
        #print miss1
        Towritepq+=(lines[i+1]+" "+str(miss1)+"\n")
                
filename="Graph/rr"+".txt"
outputFile = open(filename, 'w')
#print "\n\n\n\n"
#print Towrite
outputFile.write(Towrite)

filename="Graphpq/pq"+".txt"
outputFile = open(filename, 'w')
#print "\n\n\n\n"
#print Towritepq
outputFile.write(Towritepq)

#########################################
#getProcvsLag
Towriterrfinal = graphxy.getProcvsLag(Towrite)
outputFile = open("Gfinal/pvsl/rr.txt", 'w')
outputFile.write(Towriterrfinal)        
#########################################

#########################################
#getProcvsLag
Towritepqfinal = graphxy.getProcvsLag(Towritepq)
outputFile = open("Gfinal/pvsl/pq.txt", 'w')
outputFile.write(Towritepqfinal)        
#########################################

#########################################
#getTaskvsLag
Towriterrfinal = graphxy.getTaskvsLag(Towrite)
outputFile = open("Gfinal/tvsl/rr.txt", 'w')
outputFile.write(Towriterrfinal)        
#########################################

#########################################
#getTaskvsLag
Towritepqfinal = graphxy.getTaskvsLag(Towritepq)
outputFile = open("Gfinal/tvsl/pq1.txt", 'w')
outputFile.write(Towritepqfinal)       
#########################################

