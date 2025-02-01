import numpy as np
file = open(file='amth.txt')
texts = file.read()
for line in texts:
  words = np.array(texts.split())
list1 = []
for word in words:
  if word in list1:
    continue
  else:
    list1.append(word)
sorted_list1 = sorted(list1)
for word in sorted_list1:
  print(word)