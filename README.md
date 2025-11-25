API_REST_DJANGO

Projeto de treinamento em Django com API REST, contendo importação de banco de dados.

Conteúdo

core/ — app principal do Django

dashboard_seguranca/ — app específico para dashboard ou segurança (conforme nome)

ANTT - 14d01.csv — arquivo CSV de dados utilizados

db.sqlite3 — banco de dados SQLite usado no projeto

manage.py — script de gerenciamento do Django

Funcionalidades

Interface de API REST construída com Django / Django REST Framework (assumido por se tratar de API REST).

Importação de dados a partir de um arquivo CSV (ANTT - 14d01.csv) para a base de dados.

Estrutura de dashboards (ou componentes de segurança) no Django para visualização/monitoramento (presumido pelo nome do app dashboard_seguranca).

Tecnologias

Python

Django

Django REST Framework

SQLite como banco de dados local

Pré-requisitos

Antes de rodar o projeto, você precisa:

Ter Python instalado (versão compatível com o projeto)

Ter pip para instalar dependências

(Opcional) criar um ambiente virtual (venv ou similar)

Instalação / Setup local

Clone o repositório:

git clone https://github.com/Diego-deBrito/API_REST_DJANGO.git
cd API_REST_DJANGO


Crie e ative um ambiente virtual:

python3 -m venv venv
source venv/bin/activate     # Linux / macOS  
venv\Scripts\activate        # Windows


Instale as dependências (caso tenha um requirements.txt, senão instale manualmente Django e DRF):

pip install django djangorestframework


Aplique as migrações para configurar o banco de dados:

python manage.py migrate


(Opcional) Importe dados do CSV para o banco de dados:

Dependendo da implementação do projeto, pode haver um comando customizado ou uma rotina para isso. Se existir, por exemplo:

python manage.py import_csv "ANTT - 14d01.csv"


Se não houver, você pode abrir o Django shell e fazer a importação manualmente ou por script.

Executando a aplicação

Para rodar o servidor de desenvolvimento:

python manage.py runserver


Depois, você pode acessar:

A API REST via rotas definidas (ex: http://localhost:8000/api/...)

O painel administrativo do Django (se configurado) em http://localhost:8000/admin/

Estrutura de Rotas da API

Explique aqui os endpoints principais da sua API (exemplos):

GET /api/entidade/ — lista todos os registros

POST /api/entidade/ — cria um novo registro

PUT /api/entidade/{id}/ — atualiza um registro por ID

DELETE /api/entidade/{id}/ — deleta um registro por ID

Nota: ajuste esta seção conforme os endpoints reais do seu projeto (controllers, viewsets, serializers).

Uso

Algumas ideias de uso para esse projeto:

Experimento / protótipo de API REST com Django

Treinamento para importar dados CSV para um banco de dados via Django

Base para construir dashboards ou relatórios usando dados importados

Como contribuir

Se alguém quiser colaborar no projeto:

Faça um fork do repositório

Crie uma branch nova para sua feature ou correção

Faça os commits com mensagens claras

Abra um pull request explicando as mudanças

Licença

Defina a licença do seu projeto aqui (por exemplo, MIT, GPL, etc.). Se você não tiver definido ainda, pode adicionar algo como:

MIT License

Próximos passos / melhorias sugeridas

Algumas ideias para evoluir este projeto:

Adicionar testes automatizados (unitários e de integração) para a API

Implementar autenticação / autorização para a API (DRF)

Subir para um banco de produção (PostgreSQL, por exemplo)

Criar uma interface frontend para o dashboard de segurança

Automatizar a importação de CSV via script ou comando de management
