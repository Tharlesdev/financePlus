# 💰 FinancePlus API

API REST para controle financeiro pessoal, com autenticação via JWT, categorias e transações por usuário.

Projeto desenvolvido com foco em **boas práticas backend**, **testes de integração** e **arquitetura limpa**, ideal para estudos, portfólio e entrevistas.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.10**
* **Flask**
* **SQLAlchemy 2.0**
* **JWT (PyJWT)**
* **SQLite** (ambiente de testes)
* **PostgreSQL** (produção / futura migração)
* **Poetry** (gerenciamento de dependências)
* **Pytest** (testes de integração)

---

## 🧱 Arquitetura do Projeto

```
src/app/
│
├── app.py                # Inicialização da aplicação
├── database/             # Configuração do banco e sessão
├── externals/models/     # Models SQLAlchemy
├── services/             # Regras de negócio
├── controllers/          # Rotas / Controllers
├── security/             # JWT e autenticação
│   └── auth_required.py
└── utils/

tests/
├── integration/          # Testes de integração
└── conftest.py           # Fixtures globais
```

---

## 🔐 Autenticação

A autenticação é feita via **JWT**.

### Fluxo

1. Usuário faz login
2. API retorna um token JWT
3. Token deve ser enviado no header:

```
Authorization: Bearer <token>
```

O `user_id` é extraído **exclusivamente do token**, nunca do body da requisição.

---

## 📂 Funcionalidades

### 👤 Usuários

* Cadastro de usuário
* Login com geração de token JWT

### 🗂️ Categorias

* Criar categoria (vinculada ao usuário)
* Listar categorias do usuário

### 💸 Transações

* Criar transação (income / expense)
* Vinculada a uma categoria
* Listar transações do usuário

---

## 🧪 Testes

Os testes são **testes de integração**, validando o fluxo real da aplicação.

### Executar testes

```bash
pytest
```

Cobrem:

* Autenticação
* Rotas protegidas
* Criação e listagem de categorias
* Criação e listagem de transações

---

## ⚙️ Variáveis de Ambiente

Crie um arquivo `.env`:

```
JWT_SECRET_KEY=super_secret_key
DATABASE_URL=sqlite:///financeplus.db
```

---

## ▶️ Rodando o Projeto

```bash
poetry install
poetry shell
flask run
```

API disponível em:

```
http://localhost:5000
```

---

## 📌 Boas Práticas Aplicadas

* Separação de responsabilidades (Controller / Service / Model)
* JWT Stateless
* Ownership por usuário (user_id)
* UUID como chave primária
* Testes automatizados
* Código preparado para escalar

---

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido com foco em:

* Aprendizado de backend Python
* Preparação para entrevistas
* Demonstração de boas práticas reais de mercado

---

## 👨‍💻 Autor

**Tharles Freitas**

Projeto desenvolvido para estudos e portfólio.

---

## 📄 Licença

Este projeto é de uso educacional.
