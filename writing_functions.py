import math

# Define a function to calculate the area of an equilateral triangle
def cTa(side_length):
    area = (math.sqrt(3) / 4) * side_length ** 2
    return area

# Define a function to calculate the area of a square
def cSa(side_length):
    area = side_length ** 2
    return area

# Define a function to calculate the area of a regular pentagon
def cPa(side_length):
    area = (0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5)))) * side_length ** 2
    return area

# Define a function to calculate the area of a regular dodecagon
def cDa(side_length):
    area = 3 * (2 + math.sqrt(3)) * side_length ** 2
    return area

# Get user input for the side length
side_length = float(input("Please enter the side length: "))

# Calculate and display the areas of the specified polygons
areaT = cTa(side_length)
areaS = cSa(side_length)
areaP = cPa(side_length)
areaD = cDa(side_length)

print(f"A triangle with side {side_length:.2f} has area {areaT:.3f}")
print(f"A square with side {side_length:.2f} has area {areaS:.3f}")
print(f"A pentagon with side {side_length:.2f} has area {areaP:.3f}")
print(f"A dodecagon with side {side_length:.2f} has area {areaD:.3f}")
