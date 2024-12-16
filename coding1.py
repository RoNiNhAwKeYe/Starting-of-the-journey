def countvowels():
  f=open("sample.txt","r")
  data=f.read()
  count=0
  for i in data:
    if i in 'aeiouAEIOU':
      count+=1
      print(i)

  print("numberof vowels in sample.txt files=",count)

countvowels()
