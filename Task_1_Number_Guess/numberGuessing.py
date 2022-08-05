import random

randomNumber = random.randint(1, 100)
playerGuess = None
guesses = 0
score = 0

while(playerGuess != randomNumber):
    print("###_________________________________________________________________________###")
    playerGuess = int(input("Enter your guess:"))
    guesses += 1
    print(f'Remaining Attempt : {10-guesses}')   #remaining attempt
    if(playerGuess == randomNumber):  #checking conditions
       break
    elif(playerGuess > randomNumber):
        print("You guessed too high!")
    else:
        print("You guessed too small!")
    if(randomNumber<25):
        print("Number is less than 25")
    elif(randomNumber>25 and randomNumber<50 ):
        print("Number is in range between 25-40 ")
    if(randomNumber<75 and randomNumber>50):
        print("Number is less than 75")
    elif(randomNumber>75 and randomNumber<100 ):
        print("Number is in range between 75-100 ")
        
    if(randomNumber%2 == 0):
        print('Number you are guessing is divisible of 2 and it is also even number')   
    elif(randomNumber%3==0):
        print('And Number you are guessing is divisible of 3 and it is also odd number') 
    elif(randomNumber%5==0):
        print('And Number you are guessing is divisible of 5 ') 
    else:
        print("Number is prime")    

print("###________________________________FINAL RESULT____________________________________###")
print("***------Bingo!! You guessed the correct number------***")      
print(f'You guessed number in {guesses} attempt') # final result 
score = 10-guesses 
print(f'Your score is {score*10}%')
