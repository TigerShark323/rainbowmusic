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
    find_res = [] 
    for c in data:
        if word in c["title"]:
          find_res.append(c) 
    return find_res
posts = search (word, data)
def print_res (posts):
    for export in posts:
        print ("слово найдено в порте с id:", export["id"], "\nсодержит:", "\nid:", export["id"], "\nuserId:", export["userId"], "\nTitle:", export["title"], "\nBody:", export["body"], "\n")
    return print_res (posts)
print_res (posts)