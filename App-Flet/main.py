import flet as ft
import requests
from connect import *  # get_livros()
from urllib.parse import urlparse, parse_qs

def main(page: ft.Page):
    page.title = "Cadastro App"
    page.window.width = 400

    def show_message(text, success=True):
        page.snack_bar = ft.SnackBar(ft.Text(text))
        page.snack_bar.open = True
        page.update()

    def home_page():
        nome_input = ft.TextField(label="Nome do Produto", text_align=ft.TextAlign.LEFT)
        streaming_select = ft.Dropdown(
            options=[
                ft.dropdown.Option("Amazon Kindle", text="Amazon Kindle"),
                ft.dropdown.Option("Fisico", text="Livro Físico"),
            ],
            label="Selecione a Streaming"
        )
        lista_livros = ft.ListView()

        def cadastrar(e):
            if not nome_input.value or not streaming_select.value:
                show_message("Preencha todos os campos", success=False)
                return

            data = {
                "name": nome_input.value,
                "streaming": streaming_select.value,
                "categorie": [1]  # categorias
            }
            response = requests.post("http://localhost:8000/api/livros/", json=data)
            carregar_livros()
            if response.status_code == 200:
                show_message("Cadastro realizado com sucesso!")
            else:
                show_message("Erro ao cadastrar o produto.", success=False)

        def carregar_livros():
            lista_livros.controls.clear()
            for x in get_livros():
                lista_livros.controls.append(
                    ft.Container(
                        ft.Text(x["name"]),
                        bgcolor=ft.colors.BLACK12,
                        padding=10,
                        alignment=ft.alignment.center,
                        margin=3,
                        border_radius=10,
                        on_click=lambda e, livro_id=x["id"]: page.go(f"/review?id={livro_id}")
                    )
                )
            page.update()

        carregar_livros()
        cadastrar_btn = ft.ElevatedButton("Cadastrar", on_click=cadastrar)
        page.views.append(
            ft.View(
                "/",
                controls=[
                    nome_input, streaming_select, cadastrar_btn, lista_livros
                ]
            )
        )
        page.update()

    def review_page(livro_id):
        if livro_id is None:
            show_message("ID do livro não encontrado.", success=False)
            return

        nota_input = ft.TextField(label="Nota (inteiro)", text_align=ft.TextAlign.LEFT)
        comentario_input = ft.TextField(label="Comentário", multiline=True, expand=True)
        conteudo_atual = ft.ListView()

        def carregar_detalhes():
            conteudo_atual.controls.clear()
            for x in get_livros():
                if int(livro_id) == x["id"]:
                    conteudo_atual.controls.append(
                        ft.Container(
                            ft.Column([
                                ft.Text(f"Nome: {x['name']}"),
                                ft.Text(f"Streaming: {x['streaming']}"),
                                ft.Text(f"Nota: {x.get('note', 'N/A')}"),
                                ft.Text(f"Comentário: {x.get('comments', 'N/A')}")
                            ]),
                            bgcolor=ft.colors.BLACK12,
                            padding=10,
                            alignment=ft.alignment.center,
                            margin=3,
                            border_radius=10,
                        )
                    )
            page.update()

        def avaliar(e):
            try:
                data = {
                    "note": int(nota_input.value),
                    "comments": comentario_input.value
                }
                response = requests.put(f"http://localhost:8000/api/livros/{livro_id}", json=data)
                if response.status_code == 200:
                    show_message("Avaliação realizada com sucesso!")
                    carregar_detalhes()
                else:
                    show_message("Erro ao avaliar o livro.", success=False)
            except ValueError:
                show_message("Nota deve ser um número inteiro.", success=False)
            except Exception as ex:
                show_message(f"Erro: {ex}", success=False)
            

        carregar_detalhes()
        avaliar_btn = ft.ElevatedButton("Avaliar", on_click=avaliar)
        
        voltar_btn = ft.ElevatedButton("Voltar", on_click=lambda _: page.go("/"))
        page.views.append(
            ft.View(
                "/review",
                controls=[conteudo_atual, nota_input, comentario_input, avaliar_btn, voltar_btn]
            )
        )
        page.update()

    def route_change(e):
        page.views.clear()
        if page.route == "/":
            home_page()
        elif page.route.startswith("/review"):
            parsed_url = urlparse(page.route)
            query_params = parse_qs(parsed_url.query)
            livro_id = query_params.get("id", [None])[0]
            review_page(livro_id)
        page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(main)
