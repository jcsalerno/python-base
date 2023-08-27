import requests

def consultar_nomes(nome_pesquisado, lista_nomes):
    nomes_encontrados = []

    for nome in lista_nomes:
        if nome_pesquisado.lower() in nome.lower():
            nomes_encontrados.append(nome)

    return nomes_encontrados

def main():
    response = requests.get("https://gerador-nomes.wolan.net/nomes/10")
    
    if response.status_code == 200:
        lista_nomes = response.json()

        nome_pesquisado = input("Digite um nome para pesquisar: ")

        print("\nNomes aleatórios gerados:")
        for nome in lista_nomes:
            print(nome)

        print("\nNomes encontrados com a pesquisa:")
        nomes_encontrados = consultar_nomes(nome_pesquisado, lista_nomes)
        if nomes_encontrados:
            for nome in nomes_encontrados:
                print(nome)
        else:
            print("Nenhum nome encontrado com essa pesquisa.")
    else:
        print("Não foi possível acessar a API de nomes.")

if __name__ == "__main__":
    main()
