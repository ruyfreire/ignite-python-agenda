from utils import print_title, capture_input, print_text, colors
from list import print_contacts

def toggle_favorite(contacts):
  print_title("ADICIONAR/REMOVER CONTATO DOS FAVORITOS")

  if len(contacts) == 0:
    print_text("Nenhum contato cadastrado.", color=colors.red)
    return
  
  print_contacts(contacts)
  
  index_contact = capture_input(
    "Digite o número do contato que deseja alterar dos favoritos, ou zero para cancelar")
  
  if index_contact == "0":
    return

  index = int(index_contact) - 1
  if index < 0 or index >= len(contacts):
    print_text("Número de contato inválido.", color=colors.red)
    return

  is_favorite = contacts[index]["favorite"]
  contacts[index]["favorite"] = not is_favorite
  name = contacts[index]["name"]

  toggle_favorite = "removido" if is_favorite else "adicionado"
  print_text(f"Contato '{name}' {toggle_favorite} dos favoritos!", color=colors.green)

  return