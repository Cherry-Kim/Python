import sys,os,numpy

VAL=[]
fp=open("h.txt","r")
for line in fp:
	line_temp=line[:-1].split('\t')
	if not line_temp[0] in VAL:
		VAL.append(line_temp[:])
X = numpy.transpose(VAL)
print type(X)
numpy.savetxt("test.txt", X, fmt='%s')


