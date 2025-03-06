from src.services.encrypt import encrypt
from src.services.decrypt import decrypt
from src.services.display_menu import list_options
import unicodedata

def remove_codes(text):
  return ''.join(c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c))

first_run = True


while True:
  if first_run:
    list_options()
    choice  = input("Choose an option:")
    first_run = False
  
  if choice == "1":
    text = input("Enter your message for encrypt: ").lower()
    text = remove_codes(text)
    key = int(input("Enter your key: "))
    print("Message: ", encrypt(text, key))

  elif choice == '2':
    text = input("Enter your message for decrypt: ").lower()
    key = int(input("Enter your key: "))
    print("Message: ", decrypt(text, key))

  elif choice == 3:
    break

  return_menu = input("\nReturn menu (s/n)? ")

  if return_menu == "s":
    first_run = True
  elif return_menu == "n":
    print("Program finished!")
    break

