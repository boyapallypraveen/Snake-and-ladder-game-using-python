import random
k = 1
start = 1
end = 6
x = 0
y = 0
while(True):
  print()
  p1 = input("For player1 : ")
  m=random.randint(start, end)
  print("die is",m)
  if(x+m>100):
    print("Value exceeding 100, not possible")
  else:
    x+=m
    if(x==4):
      print("Wow! ladder to 16")
      x=16
    elif(x==32):
      print("Wow! ladder to 56")
      x=56
    elif(x==71):
      print("Wow! ladder to 91")
      x=91
    elif(x==60):
      print("Oh no! snake to 30")
      x = 30
    elif(x==99):
      print("Oh no! snake to 66")
      x = 66
    elif(x==100):
      print("Oho! player 1 won the Game")
      break
    while(m==6):
      print("player1 again: ")
      m=random.randint(start, end)
      print("die is",m)
      if(x+m>100):
        print("Value exceeding 100, not possible")
      else:
        x+=m
        if(x==4):
          print("Wow! ladder to 16")
          x=16
        elif(x==32):
          print("Wow! ladder to 56")
          x=56
        elif(x==71):
          print("Wow! ladder to 91")
          x=91
        elif(x==60):
          print("Oh no! snake to 30")
          x=30
        elif(x==99):
          print("Oh no! snake to 66")
          x=66
        elif(x==100):
          print("Oho! player 1 won the Game")
          break
  print("player 1 is at ",x)

  print()

  p2 = input("For player2 : ")
  n = random.randint(start, end)
  print("die is",n)
  if(y+n>100):
    print("Value exceeding 100, not possible")
  else:
    y+=n
    if(y==4):
      print("Wow! ladder to 16")
      y=16
    elif(y==32):
      print("Wow! ladder to 56")
      y=56
    elif(y==71):
      print("Wow! ladder to 91")
      y=91
    elif(y==60):
      print("Oh no! snake to 30")
      y = 30
    elif(y==99):
      print("Oh no! snake to 66")
      y = 66
    elif(y==100):
      print("Oho! player 2 won the Game")
      break
    while(n==6):
      print("player2 again: ")
      n=random.randint(start, end)
      print("die is",n)
      if(y+n>100):
        print("Value exceeding 100, not possible")
      else:
        y+=n
        if(y==4):
          print("Wow! ladder to 16")
          y=16
        elif(y==32):
          print("Wow! ladder to 56")
          y=56
        elif(y==71):
          print("Wow! ladder to 91")
          y=91
        elif(y==60):
          print("Oh no! snake to 30")
          y=30
        elif(y==99):
          print("Oh no! snake to 66")
          y=66
        elif(y==100):
          print("Oho! player 2 won the Game")
          break
  print("player 2 is at ",y)