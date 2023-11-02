// Observações: O nome de cada variável criada deve respeitar as regas de nomeclatura de variáveis
// Se uma variável não tiver seu valor alterado depois da inicialização, eladeve ser do tipo const
// Comece cada resolução imprimindo na tela o texto "Resultado do exercício X", sendo X o número do exercício em questão.

// Escreva um programa executando os seguintes passos:
// Crie uma variável com o valor inicial igual a 2148. Esse valor não pode ser alterado.
// Crie uma segunda variável, dessa vez sem um valor inicial
// Imprima na tela a seguinte mensagem: "O valor da primeiro é $valor", substituindo o termo inicado em $ pelo valor abrigado na sua variável.
// Atribua um valor numérico à segunda variável.
// Imprima na tela os textos "Minha segunda variável vale $valor" e "o valor da soma das minhas duas variáveis são $valor", substituindo o termno $valor pelos valores correspondentes.
// Eleve a sua segunda variável ao quadarato e imprima esse resultado na tela. Após isso, divida esse resultado por 3 e coloque-o na tela novamente.

const n1 = 2148;

console.log(n1);

let n2;

console.log(`O valor da primeiro é ${n1}`);

n2 = 7;

console.log(`Minha segunda variável vale ${n2}`);

console.log(`O valor da soma das minhas duas variáveis são ${n1 + n2}`);

console.log(Math.pow(n2, 2));

console.log(Math.pow(n2, 2) / 3);
