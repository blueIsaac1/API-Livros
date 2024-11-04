# Projeto Livros API e Cadastro App

Este projeto é uma API para gerenciar livros, permitindo a criação, avaliação e sorteio de livros. A API é construída usando o framework Ninja e Django. Além disso, o Cadastro App é uma aplicação simples desenvolvida em Python utilizando a biblioteca Flet para criar uma interface gráfica, permitindo que os usuários cadastrem livros, visualizem uma lista de livros cadastrados e avaliem esses livros.

## Instalação da API

Para instalar e executar a API, siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DA_PASTA>
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

## Rotas da API

### Criar Livro

- **POST** `/livros/`
- **Body**: 
  ```json
  {
    "name": "Nome do Livro",
    "streaming": "FI ou AK",
    "categorie": [1, 2]  // IDs das categorias
  }
  ```
- **Resposta**:
  - 200: Livro criado com sucesso.
  - 400: Erro ao criar livro.

### Avaliar Livro

- **PUT** `/livros/{livro_id}`
- **Body**:
  ```json
  {
    "note": 5,
    "comments": "Comentário sobre o livro"
  }
  ```
- **Resposta**:
  - 200: Avaliação atualizada com sucesso.
  - 404: Livro não encontrado.

### Deletar Livro

- **DELETE** `/livros/{livro_id}`
- **Resposta**:
  - 200: Livro deletado com sucesso.
  - 404: Livro não encontrado.

### Sortear Livro

- **GET** `/livros/sortear/`
- **Query Params**:
  - `nota_minima`: (opcional) Nota mínima para filtrar livros.
  - `categoria`: (opcional) ID da categoria para filtrar livros.
  - `reler`: (opcional) Booleano para incluir livros já lidos.
- **Resposta**:
  - 200: Livro sorteado.
  - 404: Nenhum livro encontrado.

## Instalação do Cadastro App

Para instalar e executar o Cadastro App, siga os passos abaixo:

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale as dependências necessárias:
   ```bash
   pip install flet requests
   ```
3. Inicie o servidor da API que fornece os dados dos livros (assumindo que está rodando em `http://localhost:8000`).
4. Execute o aplicativo:
   ```bash
   python main.py
   ```

## Funcionalidades do Cadastro App
- Cadastro de livros com nome e categoria de streaming.
- Visualização de livros cadastrados.
- Avaliação de livros com notas e comentários.
- Navegação entre a página inicial e a página de avaliação.

## Tecnologias Utilizadas
- **Python**: Linguagem de programação principal.
- **Flet**: Biblioteca para construção de interfaces gráficas.
- **Requests**: Biblioteca para fazer requisições HTTP.
- **API REST**: O aplicativo se comunica com uma API REST para armazenar e recuperar dados dos livros.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.