from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
from openpyxl import load_workbook
import pandas as pd
import time

# format code VS CODE: SHIFT + ALT + F / SHIFT + TAB = IDENTAÇÃO PARA TRÁS

opcao = 0
while opcao != 2:
    print("*" * 35)
    print("\n1 - coletar dados de um produto")
    print("2 - sair")
    opcao = int(input("\nDigite o número da opção desejada: \n"))
    print("*" * 35, "\n")

    if opcao == 1:

        loja = 0
        print("1 - TAUSTE") # Pega vários itens de uma categoria
        print("2 - MERCADO LIVRE") # Pega único item 
        loja = int(
            input("Digite o número de qual e-commerce você deseja coletar dados: "))

        if loja == 1:

            def webscraping():
                page_num = 0
                # while nav.find_elements_by_xpath('/html/body/div[7]/div[2]/section/div[3]/div/div[2]/a'):
                for x in range(clicks):
                    element = nav.find_element_by_xpath(
                        '/html/body/div[7]/div[2]/section/div[3]/div/div[2]/a')
                    nav.execute_script("arguments[0].click();", element)
                    # nav.find_element_by_xpath('/html/body/div[7]/div[2]/section/div[3]/div/div[2]/a').click()
                    # botao.send_keys("\n")
                    page_num += 1
                    print("Clicou no botão "+str(page_num))
                    time.sleep(1)

                    html = nav.page_source.encode('utf-8')

                #html = urlopen(input("\nCole aqui uma URL de um produto: "))
                bs = BeautifulSoup(html, 'html.parser')

                linhas = bs.find_all(
                    'div', {'class': 'vitrine resultItemsWrapper'})

                nomeproduto = []
                for i in linhas:
                    nome = i.findChildren("h3")
                    qtd = (len(nome))
                    cont = 0
                    while (cont < qtd):
                        nomeproduto.append(nome[cont].text)
                        cont = cont + 1

                precoproduto = []
                for i in linhas:
                    preco = i.findChildren(
                        "span", {'class': 'productCard__price--best'})
                    qtd = (len(preco))
                    cont = 0
                    while (cont < qtd):
                        precoproduto.append(preco[cont].text)
                        cont = cont + 1

                marcaproduto = []
                for i in linhas:
                    marca = i.findChildren(
                        "a", {'class': 'productCard__brand'})
                    qtd = (len(preco))
                    cont = 0
                    while (cont < qtd):
                        marcaproduto.append(marca[cont].text)
                        cont = cont + 1

                df = pd.DataFrame(
                    {'Nome': nomeproduto, 'Preço': precoproduto, 'Marca': marcaproduto})
                df.head()
                df.to_excel('Lista de Produtos Tauste.xlsx')
                print("Lista de produtos - categoria:",
                      categoria, " salvo com sucessso")
                
            nav = webdriver.Chrome()
            nav.maximize_window()
            nav.get("https://www.tauste.com.br/")

            nav.find_element_by_xpath(
                '/html/body/div[7]/div/div[2]/div[1]/div/div[1]/input').send_keys("13201-155")
            nav.find_element_by_xpath(
                '/html/body/div[7]/div/div[2]/div[1]/div/div[1]/button').click()

            print("Categorias Disponíveis: \n")
            print("1 - Adega")
            print("2 - Autos e Ferramentas")
            print("3 - Bebidas")
            print("4 - Frios e Laticínios")
            opc = int(input("Digite o número da categoria desejada: "))

            if opc == 1:
                nav.find_element_by_xpath(
                    '/html/body/div[5]/div[4]/div[1]/div/div/ul/li[1]/a/span[2]').click()  # Adega
                qtdprodutos = nav.find_element_by_xpath('/html/body/div[7]/div[2]/section/div[2]/div[1]/p/label').text
                qtd = int(qtdprodutos)
                if qtd < 500:
                    clicks = 25
                elif qtd > 500 and qtd < 700:
                    clicks = 35
                elif qtd > 700 and qtd < 1000:
                    clicks = 45
                elif qtd > 1000 and qtd < 1200:
                    clicks = 55
                else:
                    clicks = 65
                    
                categoria = "Adega"
                print("Quantidade de produtos disponíveis: ", qtdprodutos, "\ncategoria: \n", categoria)
                html = nav.page_source.encode('utf-8')
                webscraping()

            elif opc == 2:
                nav.find_element_by_xpath(
                    '/html/body/div[5]/div[4]/div[1]/div/div/ul/li[4]/a/span[2]').click()  # Autos e Ferramentas
                qtdprodutos = nav.find_element_by_xpath('/html/body/div[7]/div[2]/section/div[2]/div[1]/p/label').text
                qtd = int(qtdprodutos)
                if qtd < 500:
                    clicks = 25
                elif qtd > 500 and qtd < 700:
                    clicks = 35
                elif qtd > 700 and qtd < 1000:
                    clicks = 45
                elif qtd > 1000 and qtd < 1200:
                    clicks = 55
                else:
                    clicks = 65

                categoria = "Autos e Ferramentas"
                print("Quantidade de produtos disponíveis: ", qtdprodutos, "\ncategoria: \n", categoria)
                html = nav.page_source.encode('utf-8')
                webscraping()

            elif opc == 3:
                nav.find_element_by_xpath(
                    '/html/body/div[5]/div[4]/div[1]/div/div/ul/li[6]/a/span[2]').click()  # Bebidas
                qtdprodutos = nav.find_element_by_xpath('/html/body/div[7]/div[2]/section/div[2]/div[1]/p/label').text
                qtd = int(qtdprodutos)
                if qtd < 500:
                    clicks = 25
                elif qtd > 500 and qtd < 700:
                    clicks = 35
                elif qtd > 700 and qtd < 1000:
                    clicks = 45
                elif qtd > 1000 and qtd < 1200:
                    clicks = 55
                else:
                    clicks = 65

                categoria = "Bebidas"
                print("Quantidade de produtos disponíveis: ", qtdprodutos, "\ncategoria: \n", categoria)
                html = nav.page_source.encode('utf-8')
                webscraping()

            elif opc == 4:
                nav.find_element_by_xpath(
                    '/html/body/div[5]/div[4]/div[1]/div/div/ul/li[8]/a/span[2]').click()  # Frios e Laticínios
                qtdprodutos = nav.find_element_by_xpath('/html/body/div[7]/div[2]/section/div[2]/div[1]/p/label').text
                qtd = int(qtdprodutos)
                if qtd < 500:
                    clicks = 25
                elif qtd > 500 and qtd < 700:
                    clicks = 35
                elif qtd > 700 and qtd < 1000:
                    clicks = 45
                elif qtd > 1000 and qtd < 1200:
                    clicks = 55
                else:
                    clicks = 65

                categoria = "Frios e Laticínios"
                print("Quantidade de produtos disponíveis: ", qtdprodutos, "\ncategoria: \n", categoria)
                html = nav.page_source.encode('utf-8')
                webscraping()

            else:
                print("Categoria Inválida")

            """
            #TAUSTE

            tituloproduto = bs.find('div', {'class': 'product__name'})
            titulo = (tituloproduto.text)
            #print(titulo)

            categoriaproduto = bs.find('span', {'itemprop': 'name'})
            categoria = (categoriaproduto.text)
            #print(categoria)

            precoproduto = 2
            bs.find('strong', {'class': 'skuBestPrice'})
            preco = (precoproduto.text)
            #print(preco)

            tituloplan, categoriaplan, precoplan = [], [], []
            tituloplan.append(titulo)
            categoriaplan.append(categoria)
            precoplan.append(preco)

            df = pd.DataFrame({'Título': tituloplan, 'Categoria': categoriaplan, 'Preço': precoplan})
            df.head()
            df.to_excel('Produtos Tauste.xlsx')
            print("\nproduto", titulo, "salvo com sucesso")
            """

        elif loja == 2:

            html = urlopen(input("\nCole aqui uma URL de um produto: "))
            bs = BeautifulSoup(html, 'html.parser')

            # MERCADOLIVRE

            tituloproduto = bs.find('h1', {'class': 'ui-pdp-title'})
            titulo = (tituloproduto.text)
            # print(titulo)

            categoriaproduto = bs.find(
                'a', {'class': 'andes-breadcrumb__link'})
            categoria = (categoriaproduto.text)
            # print(categoria)

            precoproduto = bs.find('span', {'class': 'price-tag-fraction'})
            preco = (precoproduto.text)
            # print(preco)

            tituloplan, categoriaplan, precoplan = [], [], []
            tituloplan.append(titulo)
            categoriaplan.append(categoria)
            precoplan.append(preco)

            df = pd.DataFrame(
                {'Título': tituloplan, 'Categoria': categoriaplan, 'Preço': precoplan})
            df.head()
            df.to_excel('Produtos Mercado Livre.xlsx')
            print("\nproduto", titulo, "salvo com sucesso")

    elif opcao == 2:
        print("saindo")

    else:
        print("\n Opção inválida, tente novamente")

    #linhas = bs.find_all('tr', {'class':'even'})
    # print(linhas)

    """
    for i in linhas:
        print(i.text)
    ## Imprime o texto de cada uma das tags filhas ##
    for i in linhas:
        filhas = i.findChildren("td")
        print(filhas[0])
        print(filhas[1])
        print(filhas[2])

    codigo, descricao, periodo = [], [], []
    for i in linhas:
        children = i.findChildren("td")
        codigo.append(children[0].text)
        descricao.append(children[1].text)
        periodo.append(children[2].text)

    df = pd.DataFrame({'Código': codigo, 'Descrição': descricao, 'Período': periodo})
    df.head()
    df.to_excel('planilha.xlsx')
    """

    # print(bs.prettify())
    # print(bs)
