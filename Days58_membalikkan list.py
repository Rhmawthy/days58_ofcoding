A = [1,2,3,4,5]
B = [ ]

for i in range (len(A)):
	reverse_i = len(A) -1 -i
	B.append (A[reverse_i])
	
print (A)
print (B)