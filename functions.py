def average(num1, num2, num3, num4):
     total = num1 + num2 + num3 + num4 
     avg = total/4 
     return avg
print(str(average(36, 48, 60, 72)) + " is the average number")   

def cube(num1):
    cube = num1 * num1 * num1
    return cube
print(str(cube(5)) + " is the cube of 5")

def perimeter(len,wid):
    per = len + wid + len + wid
    return per
#print(str(perimeter(5, 6)) + " is the perimeter of a rectangle")

n = input("Pick a number for a length: ") 
r = input("Pick a number for a width: ") 
per = perimeter(int(n) ,int(r) )
print('the perimeter of a rectangle is ' +str(per))