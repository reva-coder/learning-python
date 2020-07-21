#volume of a cylinder

def volume (radius, height):
    return 3.14 * radius * radius * height

r = input ('give me a radius: ')
h = input ('give me a height: ')

print(type(r))
rf = float(r)
hf = float(h)
v = volume(rf, hf)
print(v)