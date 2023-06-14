from random import randint
x=-1
random_number=randint(0,10)
while x !=random_number:
    if x!=-1:
        print("wrong Guess")
        
    x=int(input("Guess the  number: "))
    
print("you guessed correctly")


    
