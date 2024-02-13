from utils import print_title, print_text, capture_input, colors
from list import print_contacts
from add import inputs_contact

def edit_contact(contacts):
  print_title("EDITAR CONTATO")

  if len(contacts) == 0:
    print_text("Nenhum contato cadastrado.", color=colors.red)
    return
  
  print_contacts(contacts)
  
  index_contact = capture_input("Digite o número do contato que deseja editar, ou zero para cancelar")

  if index_contact == "0":
    return

  index = int(index_contact) - 1
  if index < 0 or index >= len(contacts):
    print_text("Número de contato inválido.", color=colors.red)
    return

  name = contacts[index]["name"]

  print()
  print_text(f"Editando contato: {name}", color=colors.blue)
  print()

  edited = inputs_contact()

  contacts[index] = edited
  name = edited["name"]

  print_text(f"Contato '{name}' atualizado com sucesso!", color=colors.green)

  return