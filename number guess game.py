import random
secret = random.randint(1 , 50)
attempts = 0
print(" i have choose a number between 1 and 50")
while True:
  guess = int(input("enter a guess number:"))
  attempts = attempts+1
  if guess==secret:
    print("Correct,too close,well done")
  elif guess<secret:
    print("too low,try again")
  else:
    print("too high,try again")