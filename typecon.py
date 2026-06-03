#string to datatypes
val1=str(10)  #str to int
print(val1)
print(type(val1)) 

val2=str(29.9) #str to float
print(val2)
print(type(val2)) 

val3=str('true') #str to bool
print(val3)
print(type(val3)) 

val4=str(3+7j) #str to complex
print(val4)
print(type(val4))

val5=str("hello") #str to str
print(val4)
print(type(val5))


#int to float,str,bool,complex
s=1024
x=float(s) #int to float
print(x)
print(type(x)) 
d=bool(s)   #int to bool
print(d)
print(type(d))
b=str(s)    #int to str
print(b)
print(type(b))
i=complex(s)  #int to complex
print(i)
print(type(i))

#float to int,str,bool,complex
l=10.24
j=int(l) #float to int
print(j)
print(type(j))
a=str(l)  #float to str
print(a)
print(type(a))
k=bool(l)  #float to bool
print(k)
print(type(k))
p=complex(l) #float to complex
print(p)
print(type(p))

#complex to int,str,bool,float
e=3+8j
print(float(e.real)) #complex to float
print(bool(e.real))  #complex to bool
print(str(e.real))   #complex to str
print(int(e.real))   #complex to int
print(complex(e.real))  # complex to complex

