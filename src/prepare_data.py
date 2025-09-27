import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
RAW = BASE / "data" / "raw"
PROC = BASE / "data" / "processed"
PROC.mkdir(parents=True, exist_ok=True)

print(">> Leyendo datasets...")
bank_path = RAW / "bank-additional.csv"
cust_path = RAW / "customer-details.xlsx"
df_bank = pd.read_csv(bank_path)

# Leer las 3 hojas y unir
xls = pd.ExcelFile(cust_path, engine="openpyxl")
df_cust = pd.concat([pd.read_excel(xls, s) for s in xls.sheet_names], ignore_index=True)

# Normalizar nombres de columnas
def norm_cols(df):
    out = df.copy()
    out.columns = [c.strip().replace(" ", "_").replace(".", "_") for c in out.columns]
    return out

df_bank = norm_cols(df_bank)
df_cust = norm_cols(df_cust)

# Parseo simple de fechas (sin warnings)
for col in ["date", "Dt_Customer"]:
    if col in df_bank.columns:
        df_bank[col] = pd.to_datetime(df_bank[col], errors="coerce", dayfirst=True)
    if col in df_cust.columns:
        df_cust[col] = pd.to_datetime(df_cust[col], errors="coerce", dayfirst=True)

# Binarias to_bool
def to_bool(series):
    s = series.astype(str).str.strip().str.lower()
    return s.map({"yes": True, "no": False, "1": True, "0": False, "true": True, "false": False})

for col in ["default", "housing", "loan", "y"]:
    if col in df_bank.columns:
        df_bank[col] = to_bool(df_bank[col])

# Limpieza rápida
df_bank = df_bank.drop_duplicates()
df_cust = df_cust.drop_duplicates()

# Features mínimas
if "Kidhome" in df_cust.columns and "Teenhome" in df_cust.columns:
    df_cust["ChildrenTotal"] = df_cust["Kidhome"].fillna(0) + df_cust["Teenhome"].fillna(0)
    df_cust["HasChildren"] = df_cust["ChildrenTotal"] > 0

# Unión (si hay claves)
if "id_" in df_bank.columns and "ID" in df_cust.columns:
    df_merged = df_bank.merge(df_cust, left_on="id_", right_on="ID", how="left", suffixes=("", "_cust"))
else:
    df_merged = df_bank.copy()

# Guardar SOLO CSV (ligero)
df_bank.to_csv(PROC / "bank_clean.csv", index=False)
df_cust.to_csv(PROC / "customer_clean.csv", index=False)
df_merged.to_csv(PROC / "bank_customer_merged.csv", index=False)

print(">> Guardado en:", PROC.resolve())
print(">> Shapes:", df_bank.shape, df_cust.shape, df_merged.shape)

