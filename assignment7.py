#make a function that shows, how many dozens there are,
#and how many remainders there are in a number.

def doz (n):
    if n > 12:
        doze = n / 12
        print('The number has ' + str(int(doze)) + ' dozens')
    else:
        print('The number has 0 dozens')
#doz (19)

def rem (n):
    rema = n % 12
    print ('The remainder is ' + str(rema))

#rem(13)
def doz_rem (n):
    doz(n)
    rem(n)
n = input('please enter a number: ')

doz_rem(int(n))

