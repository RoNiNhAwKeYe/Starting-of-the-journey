def countconsonant():
  f=open("sample.txt","r")
  data=f.read()
  count=0
  for i in data:
      if i in 'aeiouAEIOU':
        count+=1
      else:
        count+=1
  print("number of consonants in sample.txt file=",count)

countconsonant()
    
