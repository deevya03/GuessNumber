import random

def setRange():
    range=True
    while range:
        try:
            lowerRange=int(input('Enter the lower range:'))
            upperRange=int(input('Enter the upper range:'))
            randomNumber = random.randint(lowerRange+1,upperRange-1)
            print(randomNumber)
            return lowerRange,upperRange,randomNumber
        except:
            print("Invalid input! Please try again.")


def inputNumber(lowerRange,upperRange):
    randBool = True
    while randBool: 
      try:
          guessNumber=int(input(f"Guess the number between {lowerRange} to {upperRange}: "))
          if guessNumber<=lowerRange or guessNumber>=upperRange:
              print(f"\nPlease only enter the number between the range {lowerRange} to {upperRange}")
          else:
              randBool=False
              return guessNumber
      except:
          print("\nInvalid input! Please enter again.")

    
def guessCheck(lowerRange,upperRange,randomNumber,guessNumber):
    while guessNumber!=randomNumber:
        if guessNumber>randomNumber:
            upperRange=guessNumber
            print(f'The actual number is more than {lowerRange} and less than {upperRange}')
            guessNumber=inputNumber(lowerRange,upperRange)
        elif guessNumber<randomNumber:
            lowerRange=guessNumber
            print(f"The actual number is more than {lowerRange} and less than {upperRange}")
            guessNumber=inputNumber(lowerRange,upperRange)
    print("--------------------------------------------------------")
    print(f"Yay! You have guessed the right number. The number was {randomNumber}")
    print("--------------------------------------------------------")
    
            
        

repeat=True
while repeat:
    lowerRange,upperRange,randomNumber= setRange()
    guessNumber=inputNumber(lowerRange, upperRange)
    guessCheck(lowerRange,upperRange,randomNumber,guessNumber)
    while True:
      choice=input("Enter Y to continue and N to exit:")
      if not choice:
        print("Please enter any value!")
        continue
      elif choice.upper() == "Y":
        print("Here we go again")
        print("-----------------")
        break
      elif choice.upper()=="N":
        print("--- Thank you for playing ---")
        repeat=False
        break      
      else:
        print("Please only enter the value Y or N") 
        continue
        
      
          
  
        