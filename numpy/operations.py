import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

result = numbers1 + numbers2 
result = numbers1 + 10 
result = numbers1 - numbers2 

mnumbers1 = numbers1.reshape(2,3) 
mnumbers2 = numbers2.reshape(2,3)

#print(mnumbers1,"\n")
#print(mnumbers2,"\n")
print(numbers1)
result = np.vstack((mnumbers1,mnumbers2)) # vertical
result = np.hstack((mnumbers1,mnumbers2)) # horizontal
result = numbers1 >= 50
result = numbers1 % 2 == 0 

print(numbers1[result])
print(result,"\n")
