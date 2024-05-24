# Projeto Integrador 1

## Descrição

Este projeto integrador foi desenvovido como parte do curso de Engenharia de Computação, Ciência de Dados e Tecnologia da Informação pela faculdade UNIVESP.

#### Tema norteador da UNIVESP:
Desenvolvimento de um software com framework web que utilize noções de banco de dados, praticando controler de versão.

####  Tema escolhido pelo grupo:
Desenvolver uma aplicação web que automatize a solicitação de retirada de resíduos sólidos urbanos e resíduos de construção.

## Tabela de Conteúdos
1. [Instalação](#instalação)
2. [Uso](#uso)

## Instalação

Siga os seguintes passos para configurar e executar o projeto em seu ambiente local.

### Pré-requisitos

Certifique-se de ter o python 3.6+ instalado, vocẽ pode verificar a versão do Python com o seguinte comando:
```sh
python --version
```
### Clonando o Reposiório

```sh
git clone https://github.com/Orlok97/Projeto-Integrador-1.git
```
#### Entre no diretório

```sh
cd Projeto-Integrador-1
```
### Criando e Ativando o Ambiente Virtual

```sh
#criando a venv
python -m venv nome_da_venv

#ativando a venv no Linux/macOS
source nome_da_venv/bin/activate

#ativando a venv no Windows
nome_da_venv\Scripts\activate
```

### Instalando as Dependências

Instale as dependências necessárias listada no arquivo requirements.txt:
```sh
pip install -r requirements.txt
```

### Configurando as Varíaveis de Ambiente

Crie um arquivo .env na raiz do projeto e adicione as seguintes variaveis:

```env
SECRET_KEY=SUA_CHAVE_SECRETA
DATABASE_URI=A_URI_DO_SEU_BANCO_DE_DADOS
EMAIL_USER=SEU_ENDEREÇO_DE_EMAIL #certifique-se de que seu email do google esteja configurado com vericação de duas etapas para conseguir gerar uma senha unica.
EMAIL_PASSWORD=SENHA_GERADA_PELO_GOOGLE
ADMIN_EMAIL=EMAIL_DO_ADMIN
ADMIN_PASSWORD=SENHA_DO_ADMIN
```
### Executando a Aplicação
```sh
flask run
```
## Uso

Instruções de como usar o sistema:

1. Na pagina inicial da aplicação clique no link "cadastre-se" e preencha os campos.
   
![cadastro](https://github.com/Orlok97/Projeto-Integrador-1/assets/93604560/93fbb0af-9478-407a-b41f-9365d3003844)

Se os campos forem preenchidos corretamente, o sistema vai mostrar uma mensagem que o usuario foi cadastrado com sucesso, como mostrado na imagem abaixo:
![cadastro_sucesso](https://github.com/Orlok97/Projeto-Integrador-1/assets/93604560/33a06ea3-f05f-48d9-bb68-e50620b22499)

2. Após o cadastro clique no link "login" e digite suas credencias cadastradas.

![login](https://github.com/Orlok97/Projeto-Integrador-1/assets/93604560/8af58f0a-b401-4304-ae23-94d745683f5a)

 Se as credenciais forem digitadas corretamente, o usuario será autenticado e o sistema criará uma sessão de acesso e redirecionará para pagina home onde contém as seguintes abas: Solicitar Coleta, Pendentes e Confirmadas.

 3. na aba "solicitar coleta", o usuario deve preencher o formulario com os seguintes campos: bairro, rua, região, descrição (opcional) e anexar foto (opcional).
 
![solicitando_coleta](https://github.com/Orlok97/Projeto-Integrador-1/assets/93604560/33d0a5d9-7ea0-4592-8f21-39a8c647ca9a)

4. Apoś clicar em "solicitar" o usuario pode checar a solicitação na aba "pendentes", onde mostrará uma tabela listando os dados da solicitação.

![pendentes](https://github.com/Orlok97/Projeto-Integrador-1/assets/93604560/6e1654c7-8308-4d95-b911-0f0278e8b43d)

como mostrado na imagem acima, a tabela terá uma coluna chamada "ação" onde o usuario podera editar, deletar e confirmar os dados.

ao clicar na ação "editar", o usuario pode editar os dados dos campos preenchido posteriormente no formulario da aba "Solicitar Coleta" 
![editar_solicitacao](https://github.com/Orlok97/Projeto-Integrador-1/assets/93604560/a37c864d-8e5d-46d0-9875-677e4772d22a)

ao clicar na ação "enviar" o usuario confirmará a solicitação da coleta e poderá ver os dados da coleta na aba "Confirmadas".
![solicitacao_confirmada_sucesso](https://github.com/Orlok97/Projeto-Integrador-1/assets/93604560/13a47980-e538-46e5-ac42-6c3b1f84fc30)

Após a coleta ser confirmarda um email será enviado para prefeitura contendo os dados de contato do solicitante, e os dados da coleta solicitada.
![email](https://github.com/Orlok97/Projeto-Integrador-1/assets/93604560/8a67c6c9-7003-42b3-a4a5-e3c40ca21f06)

Obs: a prefeitura também pode ter acesso aos dados de solicitação acessando a rota "/admin-login", no campo de email e senha, o administrador vai precisar digitar as credenciais que foram definidas no arquivo de configuração .env.
Ao ser autenticado o administrador será redirecionado para a rota "/admin-home" onde terá uma tabela listando todas as informações das solicitações e o contato dos usuarios que solcitaram o serviço.