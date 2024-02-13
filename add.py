from utils import print_title, capture_input, print_text, colors

def add_contact(contacts):
  print_title("NOVO CONTATO")

  new_contact = inputs_contact()

  if not new_contact:
    return

  contacts.append(new_contact)

  name = new_contact["name"]
  print_text(f"\nContato '{name}' foi adicionado com sucesso!", color=colors.green)
  return


def inputs_contact():
  name = capture_input("Nome", new_line=False)
  if name == "":
    print_text("Nome não pode ser vazio.", color=colors.red)
    return

  email = capture_input("E-mail", new_line=False)
  if email == "":
    print_text("E-mail não pode ser vazio.", color=colors.red)
    return

  phone = capture_input("Telefone", new_line=False)
  if phone == "":
    print_text("Telefone não pode ser vazio.", color=colors.red)
    return

  favorite = False
  is_favorite = capture_input("Marcar como favorito? [s/N]", new_line=False)
  if is_favorite.lower() == "s":
    print("Sim!")
    favorite = True
  else:
    print("Não!")

  contact = {
    "name": name,
    "email": email,
    "phone": phone,
    "favorite": favorite,
  }

  return contact