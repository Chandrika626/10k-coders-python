#square pattern
print("<-------🟥 SQUARE PATTERN 🟥---->")
print()
x=4
for i in range(x):
    for j in range(x):
            print("🟥",end=" ")
    print()


#right angel triangle
print()
print("<-------🌟 RIGHT ANGLE TRIANGE🌟 ------>")
print()
g = 5
for i in range(g):
    for j in range(g):
        if j <= i:
            print("🌟",end=" ")
        else:
            print(" ", end=" ")
    print()
    
#Number Triangle
print()
print("<-------❶❷❸ NUMBER TRIANGLE ❶❷❸----->")
print()
g=["❶","❷","❸","❹","❺"]
for i in range(len(g)):
    for j in range(len(g)):
        if j <= i:
            print(g[j], end=" ")
        else:
            print(" ", end=" ")
    print()
    
# repeated number triangle
print()
print("<---------1️⃣2️⃣3️⃣ REPEATED NUMBER TRIANGLE1️⃣2️⃣3️⃣---->")
print()
g=["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣"]
for i in range(len(g)):
    for j in range(len(g)):
        if j <= i:
            print(g[i],end=" ")
        else:
            print(" ", end=" ")
    print()
    
#Alphabet Triangle
print()
print("<------🄰🄱🄲 ALPHABET TRIANGLE 🄰🄱🄲---->")
print()
g = ["🄰","🄱","🄲","🄳","🄴"]
for i in range(len(g)):
    for j in range(i + 1):
        print(g[j], end=" ")
    print()
    

#inverted star triangle
print()
print("<------✵INVERTED STAR TRIANGLE✵----->")
print()
n=5
for i in range(n):
    for j in range(n):
        if j<n-i:
            print("✵",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#inverted number triangle
print()
print("<-----❶❷❸ INVERTED NUMBER TRIANGLE ❶❷❸---->")
print()
n = ["①", "②", "③", "④", "⑤"]
for i in range(len(n)):
    for j in range(len(n)):
        if j < len(n) - i:
            print(n[j], end=" ")
        else:
            print(" ", end=" ")
    print()

#continuous number pattern
print()
print("<---➀❷➂ CONTINOUS NUMBER PATTERN ➀❷➂---->")
print()
g=6
val=1
for i in range(g):
    for j in range(g):
        if j <= i:
            print(val,end=" ")
            val+=1
        else:
            print(" ", end=" ")
    print()

#right aligned star triangle
print()
print("<------☆ RIGHT ALIGNED STAR TRIANGLE ☆----->")
print()
g = 5
for i in range(g):
    for j in range(g):
        if j >=g-i-1:
            print("☆",end=" ")
        else:
            print(" ", end=" ")
    print()
    
#pyramid pattern
print()
print("<-----✶ PYRAMID PATTERN ✶------>")
n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for k in range(2 * i + 1):
        print("✶", end=" ")
    print()
    
#half butterfly wing
print()
print("<----------HALF BUTTERFLY WING------->")
print()
n=5
for i in range(n):
    for j in range(n):
        if(j==0 or i==j):
            print("✵",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n-1,-1,-1):
    for j in range(n):
        if(j==0 or i==j):
            print("✵",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#hollow pyramid pattern
n=5
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i+1):
        if(i==n-1 or j==0 or i==j):
            print("✮",end=" ")
        else:
            print(" ",end=" ")
    print()