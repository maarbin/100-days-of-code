from replit import clear
from art import logo

print(logo)
print("Welcome in the silent auction app.")

offerts = {}
start = True

while start:
  name = input("Enter name of a bidder: ")
  bid = int(input("Enter the bid price: $"))

  offerts[name] = bid

  ask = input("Are there any others bidders? Type yes or no: ").lower()
  if ask == "yes":
    clear()
  else:
    start = False
    clear()
    
highest_offer = max(offerts.values()) 
winner = max(offerts, key=offerts.get)

print(f"The winner is {winner} with bid ${highest_offer}")