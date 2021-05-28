import art #or use from art import logo
print(art.logo) 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet: #so that users can add symbols or numbers
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char #this will add the symbol or number to the text
  print(f"Here's the {cipher_direction}d result: {end_text}")

go_again = "yes"
while go_again == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift_pre = int(input("Type the shift number:\n"))
  if shift_pre > 26:
    shift = shift_pre % 26 #this accounts if the shift number inputted is beyond 26 
  caesar(start_text=text, shift_amount=shift_pre, cipher_direction=direction)
  go_again = input("Do you want to try a new cipher? Type 'Yes' or 'No' ").lower()