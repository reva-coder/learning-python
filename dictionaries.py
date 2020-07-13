foodprices = {'apple':3, 'orange':2, 'pear':1.5}
print(foodprices['pear'])
print(len(foodprices))

foodprices['watermelon'] = 7

#del foodprices['mango']
print(foodprices)

value = foodprices.pop('mango',"nada")
print(value)

value = foodprices.pop('watermelon',"nada")
print(value)

print('apple' in foodprices)

print('pineapple' not in foodprices)

foodprices.