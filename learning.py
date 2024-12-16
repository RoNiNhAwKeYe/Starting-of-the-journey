def push(stk,elem):
  stk.append(elem)
  print("Elements Inserted Successfully!!!")
  print(stk)

def pop(stk):
  if stk==[]:
    print("stack is empty")
  else:
   elep=stk.pop()
   print("Deleted element from stack is:-",elep)

def display(stk):
  if stk==[]:
    print("Stack is Empty...No Element found in stack")
  else:  
     le=len(stk)
     for i in range(le-le,-le,-le):
       print(stk[i])
stack=[]
while True:
  print(".......STACK OPERATIONS.......")
  print("1. Push")
  print("2. Pop")
  print("3. Display")
  ch=int(input("Enter your choice:-"))

  if ch==1:
     ele=int(input("Enter any number:-"))
     push(stack,ele)

  elif ch==2:
     pop(stack)

  elif ch==3:
     display(stack)

  elif ch==4:
     break
