def countconsonants():
 f=open("spider text.txt","r")
 data=f.read()
 f.close()
 count=0
 for i in data:
      if i not in 'aeiouAEIOU':
        count+=1
    
 print("number of consonants in spider text.txt",count)

countconsonants()
  
