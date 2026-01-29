#Необходимая библиотека
import requests

#Обработка запросов
example_1 = requests.get('https://api.scratch.mit.edu') #Пример GET-запроса
print(example_1.status_code) #Код статуса запроса
print(example_1.text) #Ответ запроса прямым текстом
print(example_1.json()) #Ответ запроса в виде словаря Python (если ответ не является json, то будет ошибка)
response = example_1.json()
print(response.keys()) #Все ключи в словаре
print(response['website']) #Поиск по ключу

#Запрос с заголовками
example_2 = requests.get('https://api.scratch.mit.edu/users/HexeradicalCat/messages/admin', headers={'X-Token': '43cf88901d9f4722a7e66a7795671218:MBzuLRQPRpfYhtGjqyPwut7aubk'}) #Пример запроса с авторизацией. headers - заголовки запроса

#Запрос с параметрами URL
example_3 = requests.get('https://api.scratch.mit.edu/users/polzovatel_5555/followers', params={'limit': 10})
#params - параметры URL. Да, можно сделать вот так:
example_3 = requests.get('https://api.scratch.mit.edu/users/polzovatel_5555/followers?limit=10')
#Но способ с params более безопасный и удобный

#Запрос с телом запроса
example_4 = requests.put('https://api.scratch.mit.edu/projects/1234567890', headers={'X-Token': '43cf88901d9f4722a7e66a7795671218:MBzuLRQPRpfYhtGjqyPwut7aubk'}, json={'title': 'Название проекта'})
#(Данный запрос является примером, с забаненного аккаунта чужой проект не изменить)
#Да, тут появился put. Подробнее будет ниже.
#json - тело запроса

#Методы:
url = 'https://example.com'
requests.get(url) #GET-запрос
requests.put(url) #PUT-запрос
requests.delete(url) #DELETE-запрос
requests.patch(url) #PATCH-запрос
requests.post(url) #POST-запрос
#... И так далее...

#Бонус:
import json
request = requests.get('https://scratch.mit.edu/projects/1234567890/remixtree/bare')
response = json.loads(request.text)
#Это обходной путь для request.json(), если запрос даёт ответ не в виде json, а в виде прямого текста (с деревьями ремиксов было такое дело)
