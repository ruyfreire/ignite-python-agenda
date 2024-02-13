from utils import print_title, print_text, colors

def list_contacts(contacts):
  print_title("CONTATOS")

  if len(contacts) == 0:
    print_text("Nenhum contato cadastrado.", color=colors.red)
    return

  print_contacts(contacts)
  return

def list_favorite_contacts(contacts):
  print_title("CONTATOS FAVORITOS")

  if len(contacts) == 0:
    print_text("Nenhum contato cadastrado.", color=colors.red)
    return
  
  favorite_contacts = get_favorite_contacts(contacts)

  if len(favorite_contacts) == 0:
    print_text("Nenhum contato marcado como favorito.", color=colors.red)
    return

  print_contacts(favorite_contacts)
  return

def get_favorite_contacts(contacts):
  return [contact for contact in contacts if contact["favorite"]]

def print_contacts(contacts):
  for index, contact in enumerate(contacts, start=1):
    name = contact["name"]
    email = contact["email"]
    phone = contact["phone"]
    favorite = "Sim" if contact["favorite"] else "Não"

    print_text(f"{index}. ", color=colors.purple)
    print(colors.cyan + "Nome: " + colors.reset + name)
    print(colors.cyan + "E-mail: " + colors.reset + email)
    print(colors.cyan + "Telefone: " + colors.reset + phone)
    print(colors.cyan + "Favorito: " + colors.reset + favorite)
    print_text("------------------------", color=colors.purple)