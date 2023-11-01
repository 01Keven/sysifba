**Documentação do Sistema de Cadastro de Usuários**

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
# Módulos: mysql.connector, reportlab, 

Certifique-se de ter Python 3.x instalado em seu sistema.

- Instale os módulos necessários utilizando o seguinte comando

pip install mysql-connector-python reportlab

# Configure o banco de dados MySQL com as credenciais apropriadas (host = 'localhost', usuário = 'root', senha = 'meuBanco', banco de dados = 'sysifba', port = '4306').

*Modificação no Xampp* [IMPORTANTE!!!!]

Ao configurar o ambiente de desenvolvimento no XAMPP, me deparei com um pequeno obstáculo: a porta padrão do MySQL estava conflitando com outros serviços em meu sistema. Para resolver esse problema, decidi trocar a porta padrão do MySQL para evitar qualquer interferência.

A motivação por trás dessa alteração foi assegurar que o MySQL pudesse operar sem problemas no ambiente que eu estava configurando. Com a mudança da porta, eu garantia que o MySQL e outros serviços pudessem coexistir harmoniosamente no mesmo sistema, cada um utilizando uma porta exclusiva para a comunicação.

# Passos para a Troca da Porta

Abri o painel de controle do XAMPP e naveguei até a seção de configurações do MySQL.
Localizei a opção de configuração de porta e a modifiquei para uma que não estava sendo utilizada por outros serviços.
Após fazer essa alteração, reiniciei o serviço do MySQL para aplicar as mudanças.

- Talvez seja necessario ir ate o caminho: C:\xampp\phpMyAdmin e configurar o arquivo (config.inc.php) trocando a porta e a senha se estiver vazia.

Como deve ficar:
$cfg['Servers'][$i]['port'] = 4306;
$cfg['Servers'][$i]['password'] = 'meuBanco';

**todas as portas devem ser mudadas para 4306**

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

