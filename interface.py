#interface.py
from cliente import Cliente
from banco import BancoDeDados
import os

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

meuBanco = BancoDeDados()

def limparTela():
    os.system('cls')

def pausar():
    input('Pressione [ENTER] para continuar')


def cadastrarCliente():
    nome = input('Nome: ')
    rg = input('RG: ')
    endereco = input('Endereço: ')
    email = input('Email: ')
    cidade = input('Cidade: ')
    novoCliente = Cliente(nome, rg, endereco, email, cidade)

    try:
        msg = meuBanco.salvarCliente(novoCliente)
        print(msg)
    except Exception as e:
        print('Problema com o banco. Contacte a assistência.')
        print(e)
        input()

def gerarPDF(clientes):
    pdf = SimpleDocTemplate('relatorio.pdf', pagesize=A4)
    story = []

    # Definindo os dados da tabela
    dados = [["ID", "Nome", "RG", "Endereço", "Email", "Cidade"]] + clientes

   
    tabela = Table(dados)

    # Estilizando a tabela
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    tabela.setStyle(style)
    story.append(tabela)

    # Adicionando a tabela ao PDF
    pdf.build(story)

# organizar, mais legivel
def main():
    meuBanco = BancoDeDados()
    clientes = meuBanco.visualizarClientes()

    if isinstance(clientes, list):
        gerarPDF(clientes)
        print("PDF criado com sucesso!")
    else:
        print(f"Erro ao obter os dados do banco de dados: {clientes}")

# verificando se o script está sendo executado diretamente
if __name__ == '__main__':
    main()


def visualizaRelatorio():
    ID = 0
    NOME = 1
    RG = 2
    ENDERECO = 3
    EMAIL = 4
    CIDADE = 5

    meusClientes = meuBanco.visualizarClientes()
    for umCliente in meusClientes:
        print(f'ID: {umCliente[ID]}\nNome: {umCliente[NOME]}')
        print(f'Endereço: {umCliente[ENDERECO]}')
        print(f'RG: {umCliente[RG]}')
        print(f'EMAIL: {umCliente[EMAIL]}')
        print(f'CIDADE: {umCliente[CIDADE]}')
        print('-'*50)
    

def pesquisarCliente():
    ID = 0
    NOME = 1
    RG = 2
    ENDERECO = 3
    EMAIL = 4
    CIDADE = 5

    rg = input('Digite o RG: ')

    try:
        pesquisa = meuBanco.pesquisarCliente(rg)
        for cliente in pesquisa:
            print(f'ID: {cliente[ID]} \tNome: {cliente[NOME]}')
            print(f'Endereço: {cliente[ENDERECO]}')
            print(f'RG: {cliente[RG]}')
            print(f'EMAIL: {cliente[EMAIL]}')    
            print(f'CIDADE: {cliente[CIDADE]}')    
            print('-'*50)
    except:
        print('Erro exibindo relatório')



def editarCliente():
    rg = input('Digite o RG: ')
    meuBanco.editarCliente(rg)

def excluirCliente():
    rg = input('Digite o RG: ')
    meuBanco.excluirCliente(rg)

while True:
    limparTela()
    print('=========== MENU ============')
    print('[1] - Cadastrar Cliente')
    print('[2] - Pesquisar Cliente')
    print('[3] - Relatório de Clientes')
    print('[4] - Editar Cliente')
    print('[5] - Excluir Cliente')
    print('[6] - Gerar Pdf')
    print('[0] - Sair')
    op = input('\n>> ')
    if op == '1':
        limparTela()
        print('CADASTRANDO NOVO CLIENTE')
        cadastrarCliente()
        pausar()
    elif op == '2':
        limparTela()
        print('PESQUISANDO CLIENTE')
        pesquisarCliente()
        pausar()
    elif op == '3':
        limparTela()
        print('RELATÓRIO DE CLIENTES')
        visualizaRelatorio()
        pausar()
    elif op == '4':
        limparTela()
        print('EDITAR CLIENTE')
        editarCliente()
        pausar()
    elif op == '5':
        limparTela()
        print('EXCLUIR CLIENTE')
        excluirCliente()
        pausar()
    elif op == '6':
        limparTela()
        print('Gerando pdf')
        main()
        pausar()
    elif op == '0':
        limparTela()
        print('Saindo...')
        break
    else:
        limparTela()
        print('Opção Inválida')
        pausar()