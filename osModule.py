#	See all classes affiliated with OS module

import os 

result = dir(os)
print(result)

# ----------------- # 

result = os.name
print(result)

# ----------------- #

os.chdir('C:\\')
os.chdir('../..')
os.mkdir('newdirectory')