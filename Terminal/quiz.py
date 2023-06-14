questions=[ "where is Germany?",
             "what is the capital of Germany?",
             "how many letters are in alphabet"]
answer=[ "europe",
          "berlin",
          "26"]
score=0
for i in range(0,len(questions)):
     print(questions[i])
     useranswer=input("Answer: ").lower()
     if useranswer==answer[i]:
         print("correct")
         score=score+1
     else:
         print("incorrect")
print(f"score{score}")