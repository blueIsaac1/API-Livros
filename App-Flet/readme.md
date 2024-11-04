# Cadastro App

## Descrição
O Cadastro App é uma aplicação simples desenvolvida em Python utilizando a biblioteca Flet para criar uma interface gráfica. O aplicativo permite que os usuários cadastrem livros, visualizem uma lista de livros cadastrados e avaliem esses livros com notas e comentários.

## Funcionalidades
- Cadastro de livros com nome e categoria de streaming.
- Visualização de livros cadastrados.
- Avaliação de livros com notas e comentários.
- Navegação entre a página inicial e a página de avaliação.

## Tecnologias Utilizadas
- **Python**: Linguagem de programação principal.
- **Flet**: Biblioteca para construção de interfaces gráficas.
- **Requests**: Biblioteca para fazer requisições HTTP.
- **API REST**: O aplicativo se comunica com uma API REST para armazenar e recuperar dados dos livros.

## Estrutura do Projeto
- `main.py`: Contém a lógica principal da aplicação, incluindo a interface do usuário e a interação com a API.
- `connect.py`: Contém funções para se conectar à API e obter a lista de livros.

## Como Executar
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

## Contribuição
Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, faça um fork do repositório, crie uma branch para sua feature e envie um pull request.

## Licença
Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.
