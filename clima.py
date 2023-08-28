import requests

API_KEY = "aa27bf8711585f96474c5c610097bab1"
cidade = "rio de janeiro"

link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

requesicao = requests.get(link)
requesicao_dic = requesicao.json()
descricao = requesicao_dic['weather'][0]['description']
temperatura = requesicao_dic['main']['temp'] -273.15
print(descricao, f"{temperatura}ºC")