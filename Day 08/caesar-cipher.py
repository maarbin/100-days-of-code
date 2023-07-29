alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = [' ','0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in symbols:
      end_text += char
    else:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo 
print(logo)

start = True
while start:  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  if shift > 26:
    shift = shift % 26
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  question = input("Do you want to continue? Type yes or no:\n").lower()
  if question == "no":
    start = False
    print("Goodbye")