// Escreva um programa executandos os próximos passos:
// Crie uma variável com valor inicial de um objeto que represente um pokemon (nome, estamina, defesa, ataque, habilidade).
// Imprima na tela os textos "Meu objeto pokemon possui "chave" e $valor", substituindo os termos com $ pelos valores correspondentes ao conjunto chave/valor.

const pokemon = {
  nome: "Pikachu",
  estamina: 10,
  defesa: 50,
  ataque: 100,
  habilidade: "Raio",
};

console.log(
  `Meu objeto pokemon possui o nome ${pokemon.nome} e ${pokemon.estamina} estamina`
);
console.log(
  `Meu objeto pokemon possui o nome ${pokemon.nome} e ${pokemon.defesa} defesa`
);
console.log(
  `Meu objeto pokemon possui o nome ${pokemon.nome} e ${pokemon.ataque} ataque`
);
console.log(
  `Meu objeto pokemon possui o nome ${pokemon.nome} e ${pokemon.habilidade} habilidade`
);
