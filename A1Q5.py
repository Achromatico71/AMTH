import re
file_name = input('Enter the file name')
file = open(file=file_name)
texts = file.read()
for line in texts:
  address = re.findall(r'From\s*([a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+)',texts)
print(address)