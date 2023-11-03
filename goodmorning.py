import time
t=time.strftime('%H:%M:%S')
print(t)
hour=int(time.strftime('%H'))
print()
if(hour>0 and hour<12):
  print("Good Morning")
elif(hour>12 and hour<18):
  print("Good Afternoon")
elif(hour>18 and hour<24):
  print("Good Evening")
