a=[]

choice=int(input("1->push/n 2->pop/n 3->peek/n 4->exit/n enter your choice:"))

if choice==1:
  val=int(input("30"))
  push(a.val)
def push (a):
  a.append(30)
  print("your score is 30")
if choice==2:
  if len(a)==0:
    print ("your score is 0")
  else:
    popitem(a)
def popitem(a):
  val=a.pop()
  print("bonus point",10)
if choice==3:
  if len (a)==0:
    print ("empty stack")
  else:
    peek(a)
def peek(a):
  index=len (a)-1
  print("peek elements",a[index])
