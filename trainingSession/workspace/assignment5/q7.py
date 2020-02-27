# calculate area of circle pi * r^2
def area(radius):
    return lambda pi: pi*radius*radius
print(area(7)(3.14))