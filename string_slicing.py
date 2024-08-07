#slicing is used to ge substring from string
names="Preeti, Sakshi"
print(f"String: {names}")

print(names[0:5])   #printing 0-4 elements 5th element will not print i.e last element in given range will not be print

fruit="Mango"
print(fruit)
print(len(fruit))
print(fruit[:3])    #when we don't provide starting range value then python interpreter will automatically start range from 0 index
print(fruit[:-3])   #excluding last 3 elements, in negative index we should start with last element and considering index it's index as 1 and not 0
print(fruit[:-4])

print(fruit[-1:-3]) #reverse string is not possible so nothing will print
print(fruit[-3:-1]) #this will print as string is reverse