number=int(input());
listofno=[]
for i in range(1,number//2):
    if number % i == 0:
        listofno.append(i)
sorted(listofno)
print( ", ".join( repr(e) for e in listofno) )
