import re as re

result = dir(re)

print(result)

########

# re module

string = "Python Kursu : Python Programlama Rehberiniz | 40 saat"

result = re.findall("Python", string)
print(result) 
result = len(result)
print(result)

# re.split()

result = re.split(" ", string)
print(result)
result = re.split("R", string)
print(result)

# re.sub()

result = re.sub(" ", "-",string)
print(result)
result = re.sub("\s", "-", string)
print(result)

# re.search()

result = re.search("Python",string)
print(result)
print(result.span())
print(result.start())
print(result.end())
print(result.group())
print(result.string)