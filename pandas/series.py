import pandas as pd 
import numpy as np 

# data 
numbers = [20,30,40,50]
letters = ['a','b','c','d']
scalar = 5 
dict = {'a':10, 'b':20, 'c':30, 'd':40}
random_numbers = np.random.randint(10,100,6)

pandas_series = pd.Series(numbers, ['a','b','c','d'])
result = pandas_series[3]

print(pandas_series)
print(type(pandas_series))  
print(result)