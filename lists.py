myfood=['eggs', 'coffe', 'apple', 'cheese cube']
print(myfood)

nos=[4,56,7,11,15]
print(nos)

mix=[4,11,7,25,'cat','dog',"rat"]
print(mix)

mix2=[12,2,'egg',32,'coffee',mix]
print(mix2)

myfood.append('orange')
print(myfood)

#allows to add multple items
myfood.extend(["paneer","eggplant"])
print(myfood)

#insert an item
mix.insert(0,17)
print(mix)

mix.remove('cat')
print(mix)

del nos[1]
print(nos)

#get third item from nos and add 3 to it

item=nos.pop(2)
print(item + 3)