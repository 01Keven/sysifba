
**Documentação do Sistema de Cadastro de Usuários**

------------------------------------------------------------------------------------

**Ambiente com Erros Propositais**

- Este projeto foi feito de propósito com alguns erros intencionais em certas partes do código. A ideia é mostrar como identificar e lidar com problemas que podem acontecer em programas reais. Essas mudanças foram feitas de propósito para demonstrar como reconhecer, tratar e registrar falhas da maneira certa.

# Erros que Você Pode Encontrar

1. Erro ao Salvar um Novo Usuário

    Quando você tentar cadastrar um novo cliente escolhendo a opção "Cadastrar Cliente" no menu principal, vai acontecer um erro. Isso ocorre porque uma parte do código foi alterada de propósito, causando um problema ao tentar salvar informações do usuário. O erro vai dizer que a palavra "nome" não foi definida, e essa falha será registrada em um arquivo especial chamado erros_banco.xml.

2. Erro ao Pesquisar um Cliente

    Se você tentar buscar um cliente usando a opção "Pesquisar Cliente" no menu principal e inserir um RG, vai acontecer outro erro intencional. Isso simula uma situação comum onde a busca no banco de dados é feita de forma errada. O sistema vai mostrar uma mensagem de erro indicando um problema na consulta ao banco de dados, e essa informação será registrada no arquivo erros_banco.xml.


*Onde Encontrar os Erros*

    Todas as informações sobre os erros, tanto os feitos de propósito quanto os que acontecem naturalmente, ficam registradas em um arquivo chamado erros_banco.xml. Este arquivo mostra detalhes sobre os problemas, como as mensagens de erro e quando aconteceram.

-------------------------------------------------------------------------------------

*Visão Geral*

O sysifba é uma aplicação desenvolvida em Python que permite o gerenciamento e registro de informações de usuários. Além disso, oferece a funcionalidade de exportar essas informações em formato PDF.

-------------------------------------------------------------------------------------

*Funcionalidades Principais*

Cadastro de novos usuários com os seguintes campos:

# Nome
# RG
# Endereço
# Email
# Cidade

# Visualização de todos os usuários cadastrados.

# Edição de informações de usuários existentes.

# Exclusão de usuários.

# Cadastro de novos usuarios.

# Pesquisa de usuarios ja cadastrados.

# Geração de usuarios em .pdf

-------------------------------------------------------------------------------------

*Requisitos do Sistema*

# Sistema Operacional: Windows, Linux, MacOS
# Python 3.x instalado
# Módulos: mysql.connector, reportlab, xml.etree.ElementTree, datetime

Certifique-se de ter Python 3.x instalado em seu sistema.

- Instale os módulos necessários utilizando o seguinte comando

pip install mysql-connector-python
pip install reportlab

-------------------------------------------------------------------------------------

*Utilização*

- Ao iniciar o sistema, você será apresentado com um menu com as seguintes opções:

[1] - Cadastrar Cliente
[2] - Pesquisar Cliente
[3] - Relatório de Clientes
[4] - Editar Cliente
[5] - Excluir Cliente
[6] - Gerar Pdf
[0] - Sair

Escolha a opção desejada digitando o número correspondente e siga as instruções apresentadas no console.

