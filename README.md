# ACMEVita

# Introdução

Projeto feito para o processo seletivo da [Telavita](https://www.telavita.com.br/) 

Utilizou-se Flask, SQLAlchemy e Postgres como banco de dados.

## Instalação

1. Baixar o projeto ou cloná-lo na pasta de destino.
2. Abrir o terminal e navegar até essa pasta
3. Instalar as dependências
```shell
pip install -r requirements.txt
```
4. Configurar o banco de dados:
  Dentro do arquivo .env estão as configurações do banco (host, username, password, port e database)
  Altere-o para as configurações necessárias
  
5. Execute a aplicação
```shell
python main.py
```

## Documentação

A documentação da API pode ser encontrada no [Swagger](https://app.swaggerhub.com/apis/felbarboza/ACMEVita/1.0.0)

Existem rotas para criar as entidades e popular o banco de dados, para então realizar os testes de rotas.
