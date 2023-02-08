# Desafio Jack Experts

### Essa Api foi implementada utilizando python, fastapi e banco de dados mongodb.

## Endpoints
- http://127.0.0.1:8000/people/ (get)  que retorna todas as pessoas salvas no banco de dados.
- http://127.0.0.1:8000/person/ (post) que registra um pessoa no banco de dados, no corpo dessa requisição e necessário passar um json contendo nome, valor e idade.
- http://127.0.0.1:8000/person/id (get)  que retorna uma pessoa dado os id.
- http://127.0.0.1:8000/person/?cpf="cpf" (get)  que retorna uma pessoa dado um cpf.
- http://127.0.0.1:8000/person/id (delete)  que exclui o registro de uma pessoa dado um id.
- http://127.0.0.1:8000/person/id (post) que altera os dados de uma pessoa dado um id, no corpo dessa requisição e necessário passar um json contendo nome, valor e idade.
