from utils import print_title, capture_input, print_text, colors
from list import print_contacts

def delete_contact(contacts):
  print_title("REMOVER CONTATO")

  if len(contacts) == 0:
    print_text("Nenhum contato cadastrado.", color=colors.red)
    return

  print_contacts(contacts)
  
  index_contact = capture_input("Digite o número do contato que deseja remover, ou zero para cancelar")

  if index_contact == "0":
    return
  
  index = int(index_contact) - 1
  if index < 0 or index >= len(contacts):
    print_text("Número de contato inválido.", color=colors.red)
    return

  name = contacts[index]["name"]

  should_delete = capture_input(f"Deseja realmente remover o contato {name}? [s/N]", color=colors.red)

  if should_delete.lower() != "s":
    return
  
  del contacts[index]

  print_text(f"Contato '{name}' removido com sucesso!", color=colors.green)
  return
