#calculate the area of a circle

def area_cir (radius):
    return 3.14 * radius * radius

rad = input ('give me a radius: ')
ri = int(rad)
ar = area_cir (ri)
print (ar)
