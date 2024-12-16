s=[]
c="y"
while(c=="y"):
   a=int(input("Enter any number:-"))
   c=input("Do you want to continue press'y'/'n':-")

le=len(s)
print("Elements in stack are:")
for i in range(le--1,-1,-1):
   print(s[i])
