#python 3.7.1
import random
trials=0
r=random.randrange(1,30)

def left():
  print("Only",10-(trials+1),"Attempt Left !! ")
  

while trials<10:
  n=int(input("Guess the no:"))
  if n<18:
    if r==n:
      print("Congratulations !! You Guess the No",r,"Correctly")
      print("You Guessed the Number Correctly in",trials+1,"Attempt.")
      break
    elif n<r:
      print("You guess the No Less than Magic No!!")
      left()
    elif n>r:
      print("You Gussed no to High Than Magic No !!")
      left()
    else:
      print("Game Over")
  else:
    print("Error! Tip:Enter No less than 19")
  trials+=1
