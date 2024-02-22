# Importar o módulo random
import random

# Definir as opções possíveis
opcoes = ["pedra", "papel", "tesoura"]

# Obter a escolha do usuário
usuario = input("Escolha pedra, papel ou tesoura: ")

# Validar a escolha do usuário
if usuario in opcoes:
  # Obter a escolha do computador
  computador = random.choice(opcoes)

  # Comparar as escolhas e determinar o vencedor
  resultado = ""
  if usuario == computador:
    resultado = "Empate"
  elif (
    (usuario == "pedra" and computador == "tesoura") or
    (usuario == "papel" and computador == "pedra") or
    (usuario == "tesoura" and computador == "papel")
  ):
    resultado = "Você ganhou"
  else:
    resultado = "Você perdeu"

  # Mostrar o resultado
  print("Você escolheu " + usuario)
  print("O computador escolheu " + computador)
  print(resultado)
else:
  # Mostrar uma mensagem de erro
  print("Escolha inválida")