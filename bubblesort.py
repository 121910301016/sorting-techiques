#This program is related to bubblesort technique
#ascending order
def bubblesorta(num):
  for i in range(len(num)-1,0,-1):
    for j in range(i):
      if num[j]>num[j+1]:
        temp=num[j]
        num[j]=num[j+1]
        num[j+1]=temp
#descending order
def bubblesortd(num):
  for i in range(len(num)-1,0,-1):
    for j in range(i):
      if num[j]<num[j+1]:
        temp=num[j]
        num[j]=num[j+1]
        num[j+1]=temp
num=[]
n=int(input("enter the range of the list"))
for x in range(n):
  num.append(int(input()))
bubblesorta(num)
print(num)
bubblesortd(num)
print(num)
