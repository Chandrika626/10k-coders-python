print("<--------area of square----------->")
n=int(input("enter a value:"))
Area=n*n
print("Area of square:",Area)

print()
print("<--------area of triangle----------->")
breadth=int(input("enter breadth:"))
height=int(input("enter height:"))
Area=1/2*(breadth*height)
print("Area of triangle is:",Area)

print()
print("<--------area of circle----------->")
radius=int(input("enter radius:"))
PI=3.14
Area=PI*radius*radius
print("Area of the circle is:",Area)

print()
print("<--------area of rectangle----------->")
base=int(input("enter base:"))
height=int(input("enter height:"))
Area=base*height
print("Area of rectangle is :",Area)

print()
print("<--------area of parallelogram----------->")
base=int(input("enter base:"))
perpendicular=int(input("enter perpendicular:"))
height=int(input("enter height:"))
Area=base*perpendicular*height
print("Area of parallelogram is :",Area)

print()
print("<--------AREA OF RHOMBUS----------->")
diagonal1=int(input("enter diagonal1:"))
diagonal2=int(input("enter diagonal2:"))
Area=1/2*(diagonal1*diagonal2)
print("Area of rhombus is:",Area)

print()
print("<--------AREA OF TRAPEZIM----------->")
parallel_side=int(input("enter parallel side:"))
height=int(input("enter height:"))
Area=1/2*(parallel_side*height)
print("Area of trapezium is:",Area)

print()
print("<--------AREA OF EQUILATERAL TRIANGLE----------->")
side=int(input("enter side:"))
Area=(3**0.5)/4*side*side
print("Area of equilateral triangle is:",Area)

print()
print("<--------AREA OF SECTOR OF CIRCLE ----------->")
PI=3.14
radius=int(input("enter radius:"))
angle=int(input("enter angle:"))
Area=PI*radius*radius*(angle/360)
print("Area of sector of circle is:",Area)

print()
print("<--------AREA OF SEMICIRCLE----------->")
radius=int(input("enter radius:"))
PI=3.14
Area=1/2*PI*radius**2
print("Area of semicircle is:",Area)

print()
print("<--------PERIMETER OF RECTANGLE----------->")
length=int(input("enter length:"))
breadth=int(input("enter breadth:"))
perimeter=2*(length+breadth)
print("Perimeter of rectangle is:",perimeter)

print()
print("<--------PERIMETER OF SQUARE----------->")
Area=int(input("enter Area:"))
perimeter=4*Area
print("perimeter of square is:",perimeter)

print()
print("<--------PERIMETER OF SQUARE----------->")
PI=3.14
radius=int(input("enter radius:"))
perimeter=2*PI*radius*radius
print("perimeter of circle is:",perimeter)

print()
print("<--------PERIMETER OF TRIANGLE----------->")
side=int(input("enter side:"))
side1=int(input("enter side1:"))
side2=int(input("enter side2:"))
perimeter=side+side1+side2
print("perimeter of triangle is:",perimeter)

print()
print("<--------PERIMETER OF PARALLOGRAM----------->")
Area=int(input("ente Area:"))
breadth=int(input("enter breadth:"))
perimeter=2*Area*breadth
print("perimeter of parallogram is :",perimeter)

print()
print("<--------PERIMETER OF RHOMBUS----------->")
Area=int(input("enter Area:"))
perimeter=4**Area
print("perimeter of rhombus is:",perimeter)

print()
print("<--------PERIMETER OF PENTAGON----------->")
Area=int(input("enter Area:"))
perimeter=5*Area
print("perimeter of pentagon is:",perimeter)

print()
print("<--------PERIMETER OF HEXAGON----------->")
n=int(input("enter Area:"))
perimeter=6*n
print("perimeter of hexagon is:",perimeter)

print()
print("<--------PERIMETER OF TRAPEZIUM----------->")
side=int(input("enter side:"))
side1=int(input("enter side1:"))
side2=int(input("enter side2:"))
side3=int(input("enter side3:"))
perimeter=side+side1+side2+side3
print("perimeter of trapezium is:",perimeter)

print()
print("<--------PERIMETER OF EQUILATERAL TRIANGLE----------->")
side=int(input("enter side:"))
perimeter=3*side
print("perimeter of equilateral triangle is:",perimeter)

print()
print("<--------VOLUME OF CUBE----------->")
side=int(input("enter side:"))
cube=int(input("enter cube:"))
volume=side*cube
print("volume of cube is:",volume)

print()
print("<--------TOTAL SURFACE AREA OF CUBE----------->")
side=int(input("enter side:"))
cube=6*side*2
print("surface area of cube is:",cube)

print()
print("<--------LATERAL SURFACE AREA OF CUBE----------->")
side=int(input("enter side:"))
cube=4*side*2
print("lateral surface area of cube is:",cube)

print()
print("<--------PERFECT CUBE ROOT----------->") 
perfect_cube=int(input("enter perfect cube:"))
print("cube root of perfect cube is:",perfect_cube **(1/3))

print()
print("<--------SUM OF ALL CUBES----------->")
a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
cube = a**3+b**3
print("Sum of cubes:", cube)

print()
print("<---------DIFFERENCE OF CUBE ---------->")
a=int(input("enter a value: "))
b=int(input("enter b value: "))
cube = a**3-b**3
print("diffeence of cubes in two numbers:", cube)

print()
print("<--------CUBES OF 1 TO N----------->")
n=int(input("enter n: "))
for i in range(1,n+1):
    print("cubesnumbers:",i**3)

print()
print("<--------CUBE ROOT OF A NUMBER----------->")
n=int(input("enter a number: "))
cube_root = n**(1/3)
print("Cube root of numners:", cube_root)

print()
print("<--------LARGEST CUBE----------->")
n = int(input("Enter a number: "))
i = 1
while i**3<=n:
    i+=1
print((i-1)**3)