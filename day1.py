import sys
w=10258
e=10
r="string heloo navinder to class pty"
t=True
y=5+7j
print(sys.getsizeof(w))
print(sys.getsizeof(e))
print(sys.getsizeof(r))
print(sys.getsizeof(t))
print(sys.getsizeof(y))


import sys
w=1020
e=10
r="string"
t=True
y=5+7j
print("int",(sys.getsizeof(w)))
print("float",(sys.getsizeof(e)))
print("str",(sys.getsizeof(r)))
print("bool",(sys.getsizeof(t)))
print("complex",(sys.getsizeof(y)))