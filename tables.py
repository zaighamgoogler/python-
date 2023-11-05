ques = int(input("which number's multiplication table do you want to see:"))
if(ques>=6):
  print('you can only see the tables till the number 5')
elif(ques==2):
  for i in range(1 , 11):
    print(ques ,"x",i,"=",ques*i)
elif(ques==3):
  for x in range(1 , 11):
    print(ques,"x",x,"=",ques*x)
elif(ques==4):
  for y in range(1 , 11):
    print(ques,"x",y,"=",ques*y)
elif(ques==5):
  for z in range(1 , 11):
    print(ques,"x",z,"=",ques*z)
    