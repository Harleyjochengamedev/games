// Importar o namespace System
using System;

// Definir a classe Program
class Program
{
  // Definir o método Main
  static void Main(string[] args)
  {
    // Definir as opções possíveis
    string[] opcoes = {"pedra", "papel", "tesoura"};

    // Obter a escolha do usuário
    Console.WriteLine("Escolha pedra, papel ou tesoura: ");
    string usuario = Console.ReadLine();

    // Validar a escolha do usuário
    if (Array.IndexOf(opcoes, usuario) != -1)
    {
      // Obter a escolha do computador
      Random random = new Random();
      string computador = opcoes[random.Next(opcoes.Length)];

      // Comparar as escolhas e determinar o vencedor
      string resultado = "";
      if (usuario == computador)
      {
        resultado = "Empate";
      }
      else if (
        (usuario == "pedra" && computador == "tesoura") ||
        (usuario == "papel" && computador == "pedra") ||
        (usuario == "tesoura" && computador == "papel")
      )
      {
        resultado = "Você ganhou";
      }
      else
      {
        resultado = "Você perdeu";
      }

      // Mostrar o resultado
      Console.WriteLine("Você escolheu " + usuario);
      Console.WriteLine("O computador escolheu " + computador);
      Console.WriteLine(resultado);
    }
    else
    {
      // Mostrar uma mensagem de erro
      Console.WriteLine("Escolha inválida");
    }
  }
}