import requests

def get_livros():
    response = requests.get('http://localhost:8000/api/livros/')
    if response.status_code == 200:
        livros = response.json().get('response', [])  # Supondo que o JSON tem uma chave 'response'
        return livros
    
a = get_livros()
print(a)