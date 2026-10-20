 ProjetoCursoFASTAPI

## 📌 Sobre o projeto

Este projeto foi desenvolvido durante meus estudos em desenvolvimento back-end com Python e FastAPI.

O objetivo é colocar em prática a criação de APIs REST, autenticação de usuários, integração com banco de dados e gerenciamento de pedidos.

Ao longo do desenvolvimento, foram implementadas funcionalidades de cadastro, autenticação JWT, operações com pedidos e gerenciamento de itens.

## 🛠️ Tecnologias utilizadas

- **Python** — Linguagem de programação
- **FastAPI** — Desenvolvimento da API REST
- **SQLAlchemy** — Mapeamento e manipulação do banco de dados
- **SQLite** — Banco de dados
- **Alembic** — Controle de migrações
- **Pydantic** — Validação de dados
- **Passlib / bcrypt** — Criptografia de senhas
- **JWT** — Autenticação de usuários
- **Uvicorn** — Servidor ASGI
- **Swagger UI** — Documentação e testes dos endpoints

## ⚙️ Funcionalidades

- Cadastro de usuários
- Login com e-mail e senha
- Geração de tokens JWT
- Autenticação em rotas protegidas
- Criação de pedidos
- Cancelamento de pedidos
- Listagem de pedidos
- Adição e remoção de itens
- Cálculo do valor dos pedidos

## 📂 Estrutura do projeto

```text
ProjetoCursoFASTAPI/
├── alembic/
├── main.py
├── models.py
├── schemas.py
├── dependencies.py
├── auth_routes.py
├── order_routes.py
├── alembic.ini
└── requirements.txt
```

## ▶️ Como executar

Clone o repositório e acesse a pasta do projeto.

Crie um ambiente virtual:

```bash
py -m venv .venv
```

Ative o ambiente virtual no PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure um arquivo `.env` com as variáveis:

```dotenv
SECRET_KEY=gere_uma_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Execute as migrações:

```bash
alembic upgrade head
```

Inicie a aplicação:

```bash
uvicorn main:app --reload
```

Acesse a documentação interativa:

http://127.0.0.1:8000/docs

## 📚 Aprendizados

Durante o desenvolvimento, pratiquei conceitos de APIs REST, autenticação, validação de dados, relacionamentos entre tabelas, migrações e versionamento com Git e GitHub.

O projeto faz parte do meu aprendizado em desenvolvimento de sistemas e banco de dados.

## 📌 Status

Projeto de estudos com as funcionalidades principais implementadas. Testes e melhorias continuam em andamento.
