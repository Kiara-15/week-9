import calculate

lenght = float(input("enter the lenght of the rectangle:"))
width = float(input("enter the lenght of the rectangle:"))

area = calculate.area(lenght,width)
preimeter = calculate.perimeter(lenght, width)

print(f"the area of the rectangle is: {area}")
print(f"the perimeter of the rectangle is: {preimeter}")