import json
import os.path
import sys

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados: list) -> list:
    '''
    Função para listar as categorias dos produtos presentes na lista.
    PARAMETROS: lista de dicionários representando os produtos
    RETORNO: lista contendo todas as categorias existentes nos produtos da lista de entrada
    '''
    lista_de_categorias = []
    
    for item in dados:
        if item["categoria"] not in lista_de_categorias:
            lista_de_categorias.append(item["categoria"])
    
    return lista_de_categorias

def listar_por_categoria(dados: list, categoria: str) -> list:
    '''
    Função para listar os produtos de uma categoria.
    PARAMETROS: lista de dicionários representando os produtos; uma string contendo o nome de uma categoria
    RETORNO: lista contendo todos os produtos pertencentes à categoria dada
    '''
    lista_categoria = []
    for item in dados:
        if item["categoria"] == categoria:
            lista_categoria.append(item)

    return lista_categoria
    

def produto_mais_caro(dados: list, categoria: str) -> dict:
    '''
    Função para listar o produto mais caro de uma categoria.
    PARAMETROS: lista de dicionários representando os produtos; uma string contendo o nome de uma categoria
    RETORNO: um dicionário representando o produto mais caro da categoria dada.
    '''
    lista_categoria = listar_por_categoria(dados, categoria)
    lista_ordenada_mais_caro = sorted(lista_categoria, key=lambda x: float(x["preco"]), reverse=True)

    return lista_ordenada_mais_caro[0]


def produto_mais_barato(dados: list, categoria: str) -> dict:
    '''
    Função para listar o produto mais barato de uma categoria.
    PARAMETROS: lista de dicionários representando os produtos; uma string contendo o nome de uma categoria
    RETORNO: um dicionário representando o produto mais barato da categoria dada.
    '''
    lista_categoria = listar_por_categoria(dados, categoria)
    lista_ordenada_mais_barato = sorted(lista_categoria, key=lambda x: float(x["preco"]))

    return lista_ordenada_mais_barato[0]

def top_10_caros(dados: list) -> list:
    '''
    Função para listar os 10 produtos mais caros da lista de dicionários.
    PARAMETROS: lista de dicionários representando os produtos
    RETORNO: uma lista de dicionários representando os 10 produtos mais caros.
    '''
    lista_top_10_caros = sorted(dados, key=lambda x: float(x["preco"]), reverse=True)
    return lista_top_10_caros[0:10]

def top_10_baratos(dados: list) -> list:
    '''
    Função para listar os 10 produtos mais baratos da lista de dicionários.
    PARAMETROS: lista de dicionários representando os produtos
    RETORNO: uma lista de dicionários representando os 10 produtos mais baratos.
    '''
    lista_top_10_baratos = sorted(dados, key=lambda x: float(x["preco"]))
    return lista_top_10_baratos[0:10]


def print_lista(lista: list) -> None:
    for item in lista:
        print(f"{item['id']} | R$ {item['preco']} | {item['categoria']}")

def menu(dados: list) -> None:
    ativo = 1

    while ativo == 1:
        print('''
::: LISTA DE OPÇÕES :::
[1] Listar categorias
[2] Listar produtos de uma categoria
[3] Produto mais caro por categoria
[4] Produto mais barato por categoria
[5] Top 10 produtos mais caros
[6] Top 10 produtos mais baratos
[0] Sair
        ''')

        opt = input("Digite a opção desejada: ")

        while not(opt.isdigit()):
            opt = input("Digite apenas números! Digite a opção desejada: ")

        opt = int(opt)

        if opt == 1:
            lista = listar_categorias(dados)

            print("As categorias disponíveis são:" ,(" | ").join(lista))
            ativo = 1

        elif opt == 2:
            cat = input("Digite a categoria desejada : ")
            lista_cat = sorted(listar_por_categoria(dados, cat), key= lambda x: float(x['preco']))
            print_lista(lista_cat)
            ativo = 1

        elif opt == 3:
            cat = input("Digite a categoria desejada: ")
            mais_caro = produto_mais_caro(dados, cat)
            print(f"O produto mais caro na categoria {cat} é:\n{mais_caro['id']} | R${mais_caro['preco']}")
            ativo = 1

        elif opt == 4:
            cat = input("Digite a categoria desejada: ")
            mais_barato = produto_mais_barato(dados, cat)
            print(f"O produto mais barato na categoria {cat} é:\n{mais_barato['id']} | R${mais_barato['preco']}")
            ativo = 1

        elif opt == 5:    
            lista_top_caros = top_10_caros(dados)
            print(f"--- TOP 10 PRODUTOS MAIS CAROS ---")   
            print_lista(lista_top_caros)
            ativo = 1

        elif opt == 6:
            lista_top_baratos = top_10_baratos(dados)
            print(f"--- TOP 10 PRODUTOS MAIS BARATOS ---")   
            print_lista(lista_top_baratos)
            ativo = 1

        elif opt == 0:
            print("Até mais!")
            ativo = 0

        else: 
            print("Opção inválida. Tente novamente.")
            ativo = 1



# Programa Principal - não modificar!
dados = obter_dados()
menu(dados)
