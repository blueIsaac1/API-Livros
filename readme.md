# Projeto Livros API

Este projeto é uma API para gerenciar livros, permitindo a criação, avaliação e sorteio de livros. A API é construída usando o framework Ninja e Django.

## Instalação

Para instalar e executar este projeto, siga os passos abaixo:

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

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
