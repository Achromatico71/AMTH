import re
file = open(file='mbox-short.txt')
texts = file.read()
for line in texts:
  emails = re.findall(r'From\s*([a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+)',texts)
counter = []
email_ad = []
for email in emails:
  if email in email_ad:
    continue
  else:
    email_ad.append(email)
    counter.append(emails.count(email))
for i in range(0,len(email_ad)):
  print(email_ad[i],counter[i])