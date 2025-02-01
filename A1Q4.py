import re
import numpy as np
file_name = input('Enter the file name')
file = open(file=file_name)
texts = file.read()
for line in texts:
  numbers = np.array(re.findall( r'X-DSPAM-Confidence:\s*([+-]?\d*\.\d+|\d+)',texts))
sum = 0
for number in numbers:
  sum = sum + float(number)
print(sum)