import os
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv


# -------------------------
# caminhos do projeto
# -------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

load_dotenv(BASE_DIR / "infra" / ".env")


# -------------------------
# variáveis de conexão
# -------------------------

DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5433")


DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)


# -------------------------
# caminhos dos arquivos
# -------------------------

data_path = BASE_DIR / "data" / "raw"

receitas_path = data_path / "receitas_2026.xlsx"
gastos_path = data_path / "gastos_2026.xlsx"


# -------------------------
# ingestão receitas
# -------------------------

df_receitas = pd.read_excel(receitas_path, sheet_name="receitas")

df_receitas.to_sql(
    "raw_receitas",
    engine,
    schema="public",
    if_exists="replace",
    index=False
)

print("Tabela raw_receitas carregada")


# -------------------------
# ingestão gastos
# -------------------------

df_gastos = pd.read_excel(gastos_path, sheet_name="gastos")

df_gastos.to_sql(
    "raw_gastos",
    engine,
    schema="public",
    if_exists="replace",
    index=False
)

print("Tabela raw_gastos carregada")


print("Ingestão finalizada com sucesso.")