def result(first_incourse,second_incours,attendancee,finall):
  res = (first_incourse + second_incours)/2 + attendancee + finall
  return res
txt = open(file='marks.txt')
marks = txt.readlines()
print('Roll','Letter Grade','Grade Point')
print('=== ==============  =========')
for line in marks:
  parts = line.strip().split('       ')
  roll, first_inc, second_inc, attendance, final = parts
  ress = result(int(first_inc),int(second_inc),int(attendance),int(final))
  if int(roll)<0 or int(first_inc)<0 or int(first_inc)>25 or int(second_inc)<0 or int(second_inc)>25 or int(attendance)<0 or int(attendance)>5 or int(final)<0 or int(final)>70:
    print('The number or roll is not correct!')
    continue
  if ress>=80:
    print(roll,'      A+','        4.00')
  elif ress>=75 and ress<80:
    print(roll,'      A','         3.75')
  elif ress>=70 and ress<75:
    print(roll,'      A-','        3.5')
  elif ress>=65 and ress<70:
    print(roll,'      B+','        3.25')
  elif ress>=60 and ress<65:
    print(roll,'      B','         3.00')
  elif ress>=55 and ress<60:
    print(roll,'      B-','        2.75')
  elif ress>=50 and ress<55:
    print(roll,'      C+','        2.50')
  elif ress>=45 and ress<50:
    print(roll,'      C','         2.25')
  elif ress>=40 and ress<45:
    print(roll,'      D','         0.0')
  elif ress>=0 and ress<40:
    print(roll,'      F','         0.00')
