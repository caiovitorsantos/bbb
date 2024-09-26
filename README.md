# BBB 25 - Inscrições API

API desenvolvida em Python para receber inscrições para o próximo BBB 2025

### Stacks
- Linguagem de programação: Python
- Framework web: Flask
- Banco de dados: Postgres
- Suite de testes: Pytest

### Dependencias do projeto

Foi utilizado o framework web Flask para contrstrução de uma API leve e com apenas os recursos necessários e com o 
Poetry como gerenciador de dependencias


### Configuração

Para instalar e configurar o projeto é necessário que tenha instalado na maquina Docker e docker-compose

- No terminal, dentro do diretório do projeto execute
    `docker-compose build`

- Acesse o container para rodar as migrations
    `docker-compose run app /bin/sh`

- Dentro do container da aplicação execute as migrações
    `poetry run flask db upgrade`

- Para rodar os testes, dentro do container execute:
    `poetry run pytest`

- Inicie o serviço da aplicação
    `docker-compose up`


### Endpoints

Com a aplicação rodando no endereço `http://localhost:5005`, os seguintes endpoints estão disponiveis:

GET /subscribers -> Listagem dos inscritos
[Index Success](/test_evidence/index_success.png)

POST /subscribers -> Cadastro de inscritos
[Create Success](/test_evidence/create_success.png)
[Create Falure](/test_evidence/create_failure.png)

GET /subscribers/:subscriber_id -> Detalhes do participante
[Show Success](/test_evidence/show_success.png)
[Show Not Found](/test_evidence/show_not_found.png)

PUT /subscribers/:subscriber_id -> Edição do inscrito
[Update Success](/test_evidence/update_success.png)

DELETE /subscribers/:subscriber_id -> Exclusão do inscrito
[Delete Success](/test_evidence/delete_success.png)

