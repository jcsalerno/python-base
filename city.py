import requests

API_KEY = "aa27bf8711585f96474c5c610097bab1"

def get_weather(city):
    link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=pt_br"
    requesicao = requests.get(link)
    requesicao_dic = requesicao.json()
    descricao = requesicao_dic['weather'][0]['description']
    temperatura = requesicao_dic['main']['temp'] - 273.15
    return descricao, temperatura

def main():
    print("Bem-vindo ao Bot de Previsão do Tempo!")
    
    while True:
        cidade_escolhida = input("Digite o nome da cidade que deseja verificar o clima (ou 'sair' para sair): ")
        
        if cidade_escolhida.lower() == "sair":
            print("Obrigado por usar o Bot de Previsão do Tempo. Até logo!")
            break
        
        try:
            descricao, temperatura = get_weather(cidade_escolhida)
            print(f"Condições climáticas em {cidade_escolhida.capitalize()}:")
            print(f"Descrição: {descricao.capitalize()}")
            print(f"Temperatura: {temperatura:.2f}°C")
        except:
            print("Não foi possível obter informações para a cidade fornecida. Certifique-se de que o nome da cidade esteja correto.")

if __name__ == "__main__":
    main()
