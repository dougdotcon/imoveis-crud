import flet as ft
from functions_flet import inserir_dados, buscar_imoveis, atualizar_imovel, excluir_imovel, buscar_imovel_por_id

def main(page: ft.Page):
    # Configurações da página
    page.title = "Sistema de Gestão de Imóveis"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 1200
    page.window_height = 800
    page.bgcolor = ft.colors.BLUE_GREY_50

    # Barra superior
    page.appbar = ft.AppBar(
        title=ft.Text("Sistema de Gestão de Imóveis"),
        center_title=True,
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
    )

    # Estado da aplicação
    editing_imovel_id = None

    # Campos do formulário
    tipo_negociacao = ft.Dropdown(
        label="Tipo de Negociação",
        options=[
            ft.dropdown.Option("Venda"),
            ft.dropdown.Option("Locação"),
            ft.dropdown.Option("Venda/Locação"),
        ],
        width=300,
        autofocus=True,
        border_color=ft.colors.BLUE,
    )

    status = ft.Dropdown(
        label="Status",
        options=[
            ft.dropdown.Option("Disponível"),
            ft.dropdown.Option("Locado"),
            ft.dropdown.Option("Vendido"),
            ft.dropdown.Option("À liberar"),
        ],
        width=300,
        border_color=ft.colors.BLUE,
    )

    endereco = ft.TextField(
        label="Endereço",
        multiline=True,
        min_lines=2,
        max_lines=3,
        width=300,
        border_color=ft.colors.BLUE,
    )

    tipo_imovel = ft.Dropdown(
        label="Tipo do Imóvel",
        options=[
            ft.dropdown.Option("Apartamento"),
            ft.dropdown.Option("Casa"),
            ft.dropdown.Option("Terreno"),
        ],
        width=300,
        border_color=ft.colors.BLUE,
    )

    caracteristicas = ft.TextField(
        label="Características",
        multiline=True,
        min_lines=3,
        max_lines=4,
        width=300,
        border_color=ft.colors.BLUE,
    )

    preco = ft.TextField(
        label="Preço",
        prefix_text="R$ ",
        width=300,
        keyboard_type="number",
        border_color=ft.colors.BLUE,
    )

    condicoes = ft.TextField(
        label="Condições",
        multiline=True,
        min_lines=3,
        max_lines=4,
        width=300,
        border_color=ft.colors.BLUE,
    )

    observacoes = ft.TextField(
        label="Observações",
        multiline=True,
        min_lines=3,
        max_lines=4,
        width=300,
        border_color=ft.colors.BLUE,
    )

    # Campos de pesquisa
    pesquisa_tipo = ft.Dropdown(
        label="Tipo",
        hint_text="Selecione o tipo",
        options=[
            ft.dropdown.Option(""),
            ft.dropdown.Option("Apartamento"),
            ft.dropdown.Option("Casa"),
            ft.dropdown.Option("Terreno"),
        ],
        width=200,
        border_color=ft.colors.BLUE,
    )

    pesquisa_status = ft.Dropdown(
        label="Status",
        hint_text="Selecione o status",
        options=[
            ft.dropdown.Option(""),
            ft.dropdown.Option("Disponível"),
            ft.dropdown.Option("Locado"),
            ft.dropdown.Option("Vendido"),
            ft.dropdown.Option("À liberar"),
        ],
        width=200,
        border_color=ft.colors.BLUE,
    )

    pesquisa_endereco = ft.TextField(
        label="Endereço",
        hint_text="Digite o endereço",
        width=200,
        border_color=ft.colors.BLUE,
    )

    # Mensagem de status
    status_message = ft.Text(size=16, color=ft.colors.GREEN)

    # Container para listagem
    lista_container = ft.Container(
        content=ft.Column(
            controls=[],
            scroll=ft.ScrollMode.AUTO,
            spacing=10,
        ),
        padding=20,
        expand=True,
    )

    def criar_card_imovel(imovel):
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.HOME_WORK, size=40, color=ft.colors.BLUE),
                            title=ft.Text(
                                f"{imovel['tipo_imovel']} - {imovel['tipo_negociacao']}",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                            ),
                            subtitle=ft.Text(
                                imovel['endereco'],
                                color=ft.colors.GREY_700,
                            ),
                        ),
                        ft.Divider(),
                        ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text("Status:", weight=ft.FontWeight.BOLD),
                                        ft.Text(imovel['status']),
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text("Preço:", weight=ft.FontWeight.BOLD),
                                        ft.Text(f"R$ {imovel['preco']}" if imovel['preco'] else "Não informado"),
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text("Características:", weight=ft.FontWeight.BOLD),
                                        ft.Text(imovel['caracteristicas']),
                                    ],
                                ),
                            ],
                            spacing=10,
                        ),
                        ft.Row(
                            controls=[
                                ft.OutlinedButton(
                                    "Editar",
                                    icon=ft.icons.EDIT,
                                    on_click=lambda _, id=imovel['id']: carregar_imovel_para_edicao(id),
                                    style=ft.ButtonStyle(
                                        color=ft.colors.BLUE,
                                    ),
                                ),
                                ft.OutlinedButton(
                                    "Excluir",
                                    icon=ft.icons.DELETE,
                                    on_click=lambda _, id=imovel['id']: confirmar_exclusao(id),
                                    style=ft.ButtonStyle(
                                        color=ft.colors.RED,
                                    ),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ],
                ),
                padding=20,
            ),
            elevation=4,
            margin=10,
        )

    def limpar_formulario(e=None):
        nonlocal editing_imovel_id
        editing_imovel_id = None
        tipo_negociacao.value = None
        status.value = None
        endereco.value = ""
        tipo_imovel.value = None
        caracteristicas.value = ""
        preco.value = ""
        condicoes.value = ""
        observacoes.value = ""
        page.update()

    def validar_campos():
        campos_obrigatorios = [
            tipo_negociacao.value,
            status.value,
            endereco.value,
            tipo_imovel.value,
            caracteristicas.value,
        ]
        return all(campos_obrigatorios)

    def carregar_imovel_para_edicao(id: int):
        nonlocal editing_imovel_id
        imovel = buscar_imovel_por_id(id)
        if imovel:
            editing_imovel_id = id
            tipo_negociacao.value = imovel["tipo_negociacao"]
            status.value = imovel["status"]
            endereco.value = imovel["endereco"]
            tipo_imovel.value = imovel["tipo_imovel"]
            caracteristicas.value = imovel["caracteristicas"]
            preco.value = imovel["preco"]
            condicoes.value = imovel["condicoes"]
            observacoes.value = imovel["observacoes"]
            # Mudar para a aba de cadastro
            tabs.selected_index = 0
            page.update()

    def salvar_imovel(e):
        if not validar_campos():
            status_message.value = "⚠️ Preencha todos os campos obrigatórios!"
            status_message.color = ft.colors.RED
            page.update()
            return

        try:
            if editing_imovel_id:
                sucesso = atualizar_imovel(
                    editing_imovel_id,
                    tipo_negociacao.value,
                    status.value,
                    endereco.value,
                    tipo_imovel.value,
                    caracteristicas.value,
                    preco.value,
                    condicoes.value,
                    observacoes.value,
                )
                if sucesso:
                    status_message.value = "✅ Imóvel atualizado com sucesso!"
                else:
                    status_message.value = "❌ Erro ao atualizar imóvel"
            else:
                inserir_dados(
                    tipo_negociacao.value,
                    status.value,
                    endereco.value,
                    tipo_imovel.value,
                    caracteristicas.value,
                    preco.value,
                    condicoes.value,
                    observacoes.value,
                )
                status_message.value = "✅ Imóvel cadastrado com sucesso!"
            
            status_message.color = ft.colors.GREEN
            limpar_formulario()
            atualizar_listagem()
        except Exception as e:
            status_message.value = f"❌ Erro ao salvar: {str(e)}"
            status_message.color = ft.colors.RED
        page.update()

    def confirmar_exclusao(id: int):
        def excluir():
            if excluir_imovel(id):
                dlg_confirmar.open = False
                status_message.value = "✅ Imóvel excluído com sucesso!"
                status_message.color = ft.colors.GREEN
                atualizar_listagem()
            else:
                status_message.value = "❌ Erro ao excluir imóvel"
                status_message.color = ft.colors.RED
            page.update()

        dlg_confirmar = ft.AlertDialog(
            modal=True,
            title=ft.Text("Confirmar exclusão"),
            content=ft.Text("Tem certeza que deseja excluir este imóvel?"),
            actions=[
                ft.TextButton("Cancelar", on_click=lambda _: setattr(dlg_confirmar, "open", False)),
                ft.TextButton("Excluir", on_click=lambda _: excluir()),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        page.dialog = dlg_confirmar
        dlg_confirmar.open = True
        page.update()

    def atualizar_listagem():
        filtros = {}
        if pesquisa_tipo.value:
            filtros["tipo_imovel"] = pesquisa_tipo.value
        if pesquisa_status.value:
            filtros["status"] = pesquisa_status.value
        if pesquisa_endereco.value:
            filtros["endereco"] = pesquisa_endereco.value

        imoveis = buscar_imoveis(filtros)
        
        # Limpar lista atual
        lista_container.content.controls.clear()
        
        # Adicionar cards dos imóveis
        for imovel in imoveis:
            lista_container.content.controls.append(criar_card_imovel(imovel))
        
        if not imoveis:
            lista_container.content.controls.append(
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Icon(ft.icons.SEARCH_OFF, size=64, color=ft.colors.GREY_400),
                            ft.Text(
                                "Nenhum imóvel encontrado",
                                size=16,
                                color=ft.colors.GREY_700,
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,
                )
            )
        
        page.update()

    # Botões
    bt_salvar = ft.ElevatedButton(
        "Salvar",
        icon=ft.icons.SAVE,
        on_click=salvar_imovel,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.BLUE,
            color=ft.colors.WHITE,
            padding=20,
        ),
    )

    bt_limpar = ft.OutlinedButton(
        "Limpar",
        icon=ft.icons.CLEANING_SERVICES,
        on_click=limpar_formulario,
        style=ft.ButtonStyle(
            color=ft.colors.BLUE,
            padding=20,
        ),
    )

    bt_pesquisar = ft.ElevatedButton(
        "Pesquisar",
        icon=ft.icons.SEARCH,
        on_click=lambda _: atualizar_listagem(),
        style=ft.ButtonStyle(
            bgcolor=ft.colors.BLUE,
            color=ft.colors.WHITE,
            padding=20,
        ),
    )

    # Tabs
    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Cadastro",
                icon=ft.icons.ADD_HOME_WORK,
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                content=ft.Text(
                                    "Cadastro de Imóveis",
                                    size=30,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.colors.BLUE,
                                ),
                                margin=ft.margin.only(bottom=20),
                            ),
                            ft.Divider(height=1, color=ft.colors.BLUE_100),
                            ft.Container(
                                content=ft.ResponsiveRow(
                                    controls=[
                                        ft.Column(
                                            controls=[tipo_negociacao, status, endereco],
                                            col={"sm": 12, "md": 6, "lg": 4},
                                        ),
                                        ft.Column(
                                            controls=[tipo_imovel, caracteristicas, preco],
                                            col={"sm": 12, "md": 6, "lg": 4},
                                        ),
                                        ft.Column(
                                            controls=[condicoes, observacoes],
                                            col={"sm": 12, "md": 6, "lg": 4},
                                        ),
                                    ],
                                ),
                                padding=ft.padding.all(20),
                            ),
                            ft.Container(
                                content=ft.Row(
                                    controls=[bt_salvar, bt_limpar],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                margin=ft.margin.only(top=20),
                            ),
                            status_message,
                        ],
                        scroll=ft.ScrollMode.AUTO,
                    ),
                    padding=20,
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        color=ft.colors.BLUE_GREY_100,
                        offset=ft.Offset(0, 5),
                    ),
                ),
            ),
            ft.Tab(
                text="Listagem",
                icon=ft.icons.LIST_ALT,
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                content=ft.Text(
                                    "Listagem de Imóveis",
                                    size=30,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.colors.BLUE,
                                ),
                                margin=ft.margin.only(bottom=20),
                            ),
                            ft.Divider(height=1, color=ft.colors.BLUE_100),
                            ft.Container(
                                content=ft.ResponsiveRow(
                                    controls=[
                                        ft.Column(
                                            controls=[
                                                ft.Row(
                                                    controls=[
                                                        pesquisa_tipo,
                                                        pesquisa_status,
                                                        pesquisa_endereco,
                                                        bt_pesquisar,
                                                    ],
                                                    alignment=ft.MainAxisAlignment.START,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                padding=ft.padding.all(20),
                            ),
                            lista_container,
                        ],
                    ),
                    padding=20,
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        color=ft.colors.BLUE_GREY_100,
                        offset=ft.Offset(0, 5),
                    ),
                ),
            ),
        ],
    )

    # Layout principal
    page.add(
        ft.Container(
            content=tabs,
            padding=ft.padding.all(20),
            expand=True,
        )
    )

    # Carregar listagem inicial
    atualizar_listagem()

if __name__ == "__main__":
    ft.app(target=main) 