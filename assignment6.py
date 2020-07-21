#compute area of a circle and if it is  greater than 100
#then print something

def area_cir (radius):
    return 3.14 * radius * radius
    

def big_small (area):
    if (area) < 100:
        print ('small')
    elif area >= 100 and area < 200:   
        print('medium')
    elif area >= 200:
        print('big')

rad = input ('please enter a radius: ')

ri = int(rad)
ar = area_cir (ri)

big_small(ar)