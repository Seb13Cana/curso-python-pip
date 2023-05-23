import random

def choose_options():
  options = ('piedra', 'papel','tijera')
  user_option = input('piedra, papel o tijera => ').lower()

  if not user_option in options:
    print('Opción invalida')
    return None , None

  computer_option = random.choice(options)

  print(f'Usuario escoge = {user_option}')
  print(f'Computadora escoge = {computer_option}')
  return user_option, computer_option
  

def check_rules(user_option,computer_option,user_wins,computer_wins):

  # si ambas son iguales, empate
  if user_option == computer_option:
    print ('Empate')
  # usuario escoge piedra
  elif user_option =='piedra':    
    if computer_option == 'papel':
      print('Papel cubre Piedra')
      print('Computadora gana')
      computer_wins = computer_wins + 1
    elif computer_option == 'tijera':
      print('Piedra rompe tijeras')
      print('usuario gana')
      user_wins = user_wins + 1
  # Usuario escoge papel
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('user gano')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('computer gano!')
      computer_wins += 1
  #usuario escoge tijera
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('user gano!')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('computer gano!')
      computer_wins += 1
  return user_wins, computer_wins 

  
def run_game():
  # variables de las victorias
  user_wins = 0
  computer_wins = 0
  rounds = 1
  while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print(f'Victorias de la computadora {computer_wins}')
    print(f'Victorias del usuario {user_wins}')
    rounds += 1

    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

    if computer_wins == 2:
      print('El ganador es la computadora')
      break

    if user_wins == 2:
      print('El ganador es el usuario')
      break

run_game()
