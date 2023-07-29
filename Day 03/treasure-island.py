print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

a1 = input("Your adventure begins at the crossroad. Which road do you choose? Type 'left' or 'right': ").lower()

if a1 == "left":
  a2 = input("You see a river at the end of the road.There is a harbor, but you don't see a boat. What do you do? Type 'swim' or 'wait': ")
  if a2 == "wait":
    a3 = input("After an hour you see boat on the horizon. Now you can swim through the river. When you left the boat you see a castle with three doors. Which one you choose? Type 'red', 'blue' or 'yellow': ")
    if a3 == "yellow":
      print("You found gold! You win!")
    elif a3 == "red":
      print("You found only fire! Game over")
    elif a3 == "blue":
      print("You found hungry beast! Game over")
    else:
      print("What? Game over!")
  else:
    print("Ooops! You are attacked by a trout. Game over")
else:
  print("Ooops! You fall into a hole. Game over")
