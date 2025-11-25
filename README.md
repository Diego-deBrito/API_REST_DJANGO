# Dashboard de Postura de Segurança (CISO)

Este projeto consiste em uma API REST desenvolvida com Django Rest Framework (DRF) que alimenta um dashboard visual para monitoramento de indicadores de segurança (KPIs). O sistema processa dados históricos de ambientes On-Premise e Azure, permitindo a visualização da evolução de riscos, compliance de senhas e higiene do Active Directory.

## Funcionalidades Principais

- **API RESTful:** Endpoints para consulta de métricas de segurança.
- **Importação de Dados:** Script automatizado para ingestão de dados via arquivos CSV.
- **Dashboard Interativo:** Frontend desacoplado utilizando Chart.js para renderização de gráficos.
- **Documentação Automática:** Swagger/OpenAPI integrado via drf-spectacular.
- **Métricas Monitoradas:**
    - Sistemas Operacionais de Risco.
    - Contas de Administrador (Privileged Access).
    - Higiene de Contas (Usuários Obsoletos/Stale).
    - Conformidade de Senhas.
    - Bloqueios de Conta (Lockouts).

## Tecnologias Utilizadas

- **Backend:** Python 3, Django 5, Django Rest Framework.
- **Documentação:** drf-spectacular (OpenAPI 3.0).
- **Frontend:** HTML5, CSS3, Chart.js (consumindo JSON da API).
- **Banco de Dados:** SQLite (padrão) ou compatível com Django ORM.

## Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina.

## Instalação e Configuração

1. Clone o repositório:
```bash
git clone [https://github.com/seu-usuario/dashboard-seguranca.git](https://github.com/seu-usuario/dashboard-seguranca.git)
cd dashboard-seguranca
Crie e ative o ambiente virtual:

Bash

# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
Instale as dependências:

Bash

pip install django djangorestframework django-filter drf-spectacular
Execute as migrações do banco de dados:

Bash

python manage.py makemigrations
python manage.py migrate
Importação de Dados
O projeto possui um comando personalizado para carregar os dados da planilha ANTT - 14d01.csv.

Coloque o arquivo .csv na raiz do projeto (mesma pasta do manage.py).

Execute o comando de importação:

Bash

python manage.py importar_csv
Caso precise limpar o banco antes de importar novos dados:

Bash

python manage.py flush
Executando o Projeto
Inicie o servidor de desenvolvimento:

Bash

python manage.py runserver
Acesse os seguintes endereços no navegador:

Dashboard Visual: https://www.google.com/search?q=http://127.0.0.1:8000/

API Root: https://www.google.com/search?q=http://127.0.0.1:8000/api/metricas/

Documentação Swagger: https://www.google.com/search?q=http://127.0.0.1:8000/api/docs/

Endpoints da API
Métricas de Segurança
GET /api/metricas/: Lista todo o histórico de métricas.

GET /api/metricas/?dominio=antt.gov.br: Filtra métricas por domínio.

Dados do Dashboard
GET /api/metricas/dashboard_data/: Retorna um JSON estruturado especificamente para alimentar os gráficos do frontend, contendo séries temporais separadas por categorias (risco, gestão, kpis).

Estrutura do Projeto
core/models.py: Definição da estrutura do banco de dados para os KPIs.

core/views.py: Lógica da API e tratamento dos dados para o dashboard.

core/management/commands/importar_csv.py: Script ETL para leitura do CSV.

templates/index.html: Interface do dashboard com Chart.js.

Licença
Este projeto é destinado a fins de estudo e monitoramento interno.
