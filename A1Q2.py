import re
import numpy as np
file = open(file="regex-sum-42.txt")
texts = file.read()
for line in texts:
  numbers = np.array(re.findall('[0-9]+',texts))
sum = 0
for i in numbers:
  sum = sum + int(i)
print(sum)