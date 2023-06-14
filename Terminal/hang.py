
maxguess=10
tries=0
words="Country"
word=words.lower()

print(word)

while True:
    key =input("Guess Letter:  ").lower()
    if key in word:
      print(word+" contains "+key)
      word=word.replace(key,'')
      print(len(word))
      
      if len(word)==0:
          print("you win")
          break
    else:
         print("wrong")
         tries=tries+1
         if tries>=maxguess:
             print("you lost")
             break
    


