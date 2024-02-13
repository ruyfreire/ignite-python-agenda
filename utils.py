import os

class colors:
  red = '\033[31m'
  green = '\033[32m'
  blue = '\033[34m'
  purple = '\033[35m'
  yellow = '\033[93m'
  cyan = '\033[36m'
  reset = '\033[0m'

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def print_title(text, clear_screen=True):
  if clear_screen:
    clear()

  print(colors.blue, "\n" + "=" * len(text))
  print(text)
  print("=" * len(text), colors.reset)

def print_text(text, color=colors.reset):
  if color == colors.reset:
    print(text)
  else:
    print(color + text + colors.reset)

def capture_input(label, color=colors.yellow, new_line=True):
  text = f"\n{label}: " if new_line else f"{label}: "
  print(color + text + colors.reset, end="")
  return input()

def load_contacts():
  try:
    file = open("contacts.txt", "r")
    lines = file.readlines()
    file.close()
  except FileNotFoundError:
    return []

  contacts = []

  for line in lines:
    name, email, phone, favorite = line.strip().split(",")
    contact = {
      "name": name,
      "email": email,
      "phone": phone,
      "favorite": favorite == "True",
    }
    contacts.append(contact)

  return contacts

def save_contacts(contacts):
  try:
    file = open("contacts.txt", "w")

    for contact in contacts:
      name = contact["name"]
      email = contact["email"]
      phone = contact["phone"]
      favorite = contact["favorite"]
      file.write(f"{name},{email},{phone},{favorite}\n")
  except Exception as error:
    print_text(f"Erro ao salvar contatos: {error}", color=colors.red)

  file.close()
