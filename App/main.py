import requests

result = requests.get ('https://jsonplaceholder.typicode.com/posts')
coderesult = result.status_code
if coderesult > 200:
    print (coderesult, "проблемы соединения с сервером")
else:
    coderesult = 200
word = input ("Введите фразу для поиска:")
data = result.json()
def search (word, data):
    for c in data:
        if word in c["title"]:
            print ("данное слово содержится в тайтле поста", c["id"], "\n", "содержание поста:", c)
search(word, data)