# Projeto Integrador 1

## Descrição

Este projeto integrador foi desenvovido como parte do curso de Engenharia de Computação, Ciência de Dados e Tecnologia da Informação pela faculdade UNIVESP.

#### Tema norteador da UNIVESP:
Desenvolvimento de um software com framework web que utilize noções de banco de dados, praticando controler de versão.

####  Tema escolhido pelo grupo:
Desenvolver uma aplicação web que automatize a solicitção de retirada de resíduos sólidos urbanos e resíduos de contrução.

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
#### entre na diretorio

```sh
cd Projeto-Integrador-1
```
### Criando e Ativando o Ambiente Virtual

```sh
#criando a venv
python -m venv nome_da_venv
#ativando a venv
source nome_da_venv/bin/activate
#ativando a venv no windows
nome_da_venv\Scripts\Activate
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

1. na pagina inicia clique no link "cadastre-se" e preencha os campos


 
