# TW Clients

Projeto feito durante o curso [Django Fundamentos](https://www.treinaweb.com.br/curso/django-fundamentos) da [TreinaWeb](http://treinaweb.com.br/).

## Bibliotecas utilizadas

- Django
- python-decouple
- dj-database-url

## Requisitos

- Python 3.6 ou superior

## Como começar

Clone este repositório e entre na pasta do projeto

```bash
git clone https://github.com/CleysonPH/tw_clients.git
cd tw_clients
```

## Como rodar esse projeto

Crie e ative um ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

Instale as dependências do projeto

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz do projeto com as informações do banco de dados, use o arquivo `.env_exemple` como base.

Rode as migrações para cirar o banco de dados

```bash
python manage.py migrate
```

E por ultimo basta executar o servidor de desenvolvimento do Django

```bash
python manage.py runserver
```

E então acesse a aplicação em http://localhost:8000/

## Rotas disponiveis

| Métodos HTTP | Rota                        |
|--------------|-----------------------------|
| GET          | /clientes/listar            |
| GET, POST    | /clientes/cadastrar         |
| GET          | /clientes/\<int:pk>/detalhes|
| GET, POST    | /clientes/\<int:pk>/editar  |
| GET          | /clientes/\<int:pk>/deletar |

## Estrutura do Projeto

```bash
.
├── .env_example
├── .gitignore
├── clients
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── clients
│   │       ├── client_confirm_delete.html
│   │       ├── client_detail.html
│   │       ├── client_form.html
│   │       └── client_list.html
│   ├── templatetags
│   │   └── filters.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── README.md
├── requirements-dev.txt
├── requirements.txt
├── static
│   └── css
│       └── styles.css
├── templates
│   └── base.html
└── tw_clients
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```