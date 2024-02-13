from utils import print_title, capture_input, print_text, colors, load_contacts, save_contacts
from add import add_contact
from list import list_contacts, list_favorite_contacts
from edit import edit_contact
from favorite import toggle_favorite
from delete import delete_contact

contacts = load_contacts()

while True:
  print_title("AGENDA DE CONTATOS", clear_screen=False)

  print("1. Adicionar contato")
  print("2. Ver contatos")
  print("3. Ver contatos favoritos")
  print("4. Editar contato")
  print("5. Adicionar/Remover contato dos favoritos")
  print("6. Apagar contato")
  print("0. Sair")

  option = capture_input("Escolha uma opção")

  if option == "1":
    add_contact(contacts)

  elif option == "2":
    list_contacts(contacts)

  elif option == "3":
    list_favorite_contacts(contacts)

  elif option =="4":
    edit_contact(contacts)

  elif option == "5":
    toggle_favorite(contacts)

  elif option == "6":
    delete_contact(contacts)

  elif option == "0":
    save_contacts(contacts)
    break

  else:
    print_text("Opção inválida", color=colors.red)

print_title("AGENDA FECHADA", clear_screen=False)