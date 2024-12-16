def countvowels():
  f=open("spider text.txt","r")
  data=f.read()
  count=0
  for i in data:
    if i in 'aeiouAEIOU':
      count+=1
      print(i)

  print("number of vowels in spider text.txt files=",count)

countvowels()
