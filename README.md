# Pipeline de Dados de Finanças Pessoais

---

## 1. Sobre o Projeto

Este projeto implementa um **pipeline simples de engenharia de dados** para análise de finanças pessoais.

O pipeline ingere dados financeiros armazenados em planilhas Excel, carrega essas informações em um banco de dados PostgreSQL e permite consultas analíticas para entender receitas, gastos e padrões de consumo.

O objetivo é demonstrar conceitos fundamentais de engenharia de dados, incluindo ingestão de dados, modelagem em banco relacional e consultas analíticas.

---

## 2. Problema que o Projeto Resolve

Gerenciar finanças pessoais apenas com planilhas pode dificultar:

* Analisar padrões de gastos
* Acompanhar despesas mensais
* Entender quanto se gasta por categoria
* Comparar receitas e despesas ao longo do tempo

Este projeto resolve o problema ao transformar dados de planilhas em um **banco de dados estruturado**, permitindo consultas e análises mais eficientes.

---

## 3. Arquitetura e Fluxo de Dados

O pipeline segue uma arquitetura **ELT (Extract, Load, Transform)**.

```
Planilhas Excel
      ↓
Script de ingestão em Python
      ↓
Banco de dados PostgreSQL (tabelas raw)
      ↓
Consultas analíticas SQL
```

### Etapas do pipeline

1. Os dados financeiros são armazenados em planilhas Excel.
2. Um script em Python lê os arquivos utilizando Pandas.
3. Os dados são carregados no PostgreSQL em tabelas da camada **raw**.
4. Consultas SQL permitem realizar análises financeiras.

---

## 4. Tecnologias Utilizadas

### Linguagens e Ferramentas

* Python
* PostgreSQL
* Docker
* Git

### Bibliotecas Python

* pandas
* openpyxl
* sqlalchemy
* psycopg2-binary
* python-dotenv

---

## 5. Estrutura do Projeto

```
project/
│
├── data/
│   └── raw/                         # Planilhas Excel (não versionadas)
│       ├── receitas_2026.xlsx
│       └── gastos_2026.xlsx
│
├── infra/
│   ├── docker-compose.yml
│   └── .env.example
│
├── src/
│   ├── ingestion/
│   │   └── ingest_financeiro.py     # Script de ingestão
│   │
│   ├── analytics/
│   │   └── sql/                     # Queries analíticas em SQL
│   │
│   └── transformation/
│
└── requirements.txt
```

---

## 6. Aviso sobre os Dados

Os arquivos de dados financeiros (`receitas_2026.xlsx` e `gastos_2026.xlsx`) **não estão versionados** por conter informações pessoais.

Para testar e replicar o pipeline, o usuário deve:

1. Criar suas próprias planilhas com o mesmo formato esperado pelo script de ingestão:
   * Aba `receitas` com colunas: `entradas`, `valor`, `data`, `descricao`, `mes`
   * Aba `gastos` com colunas: `data`, `valor`, `item`, `tipo_pagamento`, `mes`
2. Colocar os arquivos na pasta `data/raw/`.
3. Executar o script de ingestão normalmente.

---

## 7. Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/friszao-dev/personal-finance-pipeline.git
```

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar as variáveis de ambiente

* Renomeie `infra/.env.example` para `infra/.env`
* Ajuste as credenciais conforme necessário

### 5. Subir o banco PostgreSQL com Docker

```bash
cd infra
docker compose up -d
```

### 6. Executar o script de ingestão

```bash
python src/ingestion/ingest_financeiro.py
```

Após a execução serão criadas duas tabelas no banco:

* `raw_receitas`
* `raw_gastos`

---

## 8. Próximos Passos / Melhorias Futuras

* Criar camadas staging e mart
* Automatizar a ingestão de dados
* Criar dashboards (Power BI, Metabase ou outra ferramenta)
* Adicionar validação de qualidade de dados
* Implementar transformações com dbt

---

## 9. Objetivos de Aprendizado

Este projeto demonstra conceitos importantes de engenharia de dados:

* Construção de pipelines de dados (ELT)
* Ingestão de dados com Python e Pandas
* Modelagem em banco relacional
* Consultas analíticas em SQL
* Infraestrutura dockerizada

---