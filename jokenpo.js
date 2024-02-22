// Definir as opções possíveis
var opcoes = ["pedra", "papel", "tesoura"];

// Obter a escolha do usuário
var usuario = prompt("Escolha pedra, papel ou tesoura");

// Validar a escolha do usuário
if (opcoes.includes(usuario)) {
  // Obter a escolha do computador
  var computador = opcoes[Math.floor(Math.random() * opcoes.length)];

  // Comparar as escolhas e determinar o vencedor
  var resultado = "";
  if (usuario === computador) {
    resultado = "Empate";
  } else if (
    (usuario === "pedra" && computador === "tesoura") ||
    (usuario === "papel" && computador === "pedra") ||
    (usuario === "tesoura" && computador === "papel")
  ) {
    resultado = "Você ganhou";
  } else {
    resultado = "Você perdeu";
  }

  // Mostrar o resultado
  alert("Você escolheu " + usuario + "\nO computador escolheu " + computador + "\n" + resultado);
} else {
  // Mostrar uma mensagem de erro
  alert("Escolha inválida");
}