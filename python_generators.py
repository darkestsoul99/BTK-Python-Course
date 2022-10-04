# Generators are used for memory efficiency. When we have 
# to get a value for one-time use, we can use generators 
# to avoid an unnecessary list creation. 'yield' only 
# returns the value one time and it is not saved in memory. 


# Generators can be used with the 'yield'
def cube():
	for i in range(5):
		yield i**3 

generator = cube()

iterator = iter(generator)

# Print each 
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# for loop
for i in cube():
	print(i)

# Generators can be described as follow
generator = (i**3 for i in range(5))
print(generator)
print(next(generator))
print(next(generator))