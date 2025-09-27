# Proyecto EDA con Python – Bank Marketing

**Fecha:** 2025-09-25

Este repositorio contiene un análisis exploratorio de datos (EDA) sobre campañas de marketing directo de una entidad bancaria portuguesa.
Incluye dos datasets:
- `bank-additional.csv` (campañas y variables socioeconómicas)
- `customer-details.xlsx` (tres hojas con detalles de clientes)

## Estructura
```
.
├── data
│   ├── raw
│   │   ├── bank-additional.csv
│   │   └── customer-details.xlsx
│   └── processed
├── notebooks
│   └── 01_EDA.ipynb
├── reports
│   └── (gráficos / tablas exportadas)
├── src
│   ├── prepare_data.py
│   └── utils.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Cómo ejecutar

1. **Crear entorno y activar** (ejemplo con venv):
   ```bash
   python -m venv .venv
   # Windows: .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Generar datos procesados** (transformaciones básicas y unión de datasets):
   ```bash
   python src/prepare_data.py
   ```

4. **Abrir el notebook y ejecutar el EDA**:
   ```bash
   # Si usas VS Code, abre el proyecto y ejecuta el notebook 01_EDA.ipynb
   # O bien con Jupyter:
   jupyter notebook notebooks/01_EDA.ipynb
   ```

## Notas metodológicas

- Se realiza limpieza de nulos/duplicados, tipificación de columnas (fechas, enteros, categorías) y unión (`id_` ↔ `ID`).
- Se guardan datasets transformados en `data/processed/` en CSV y Parquet.
- En el notebook se incluyen estadísticas descriptivas y visualizaciones (histogramas, boxplots, barras, correlaciones).
- Al final se listan **insights** y **conclusiones**.

## Entrega en GitHub

1. Inicia repositorio y primer commit:
   ```bash
   git init
   git add .
   git commit -m "Init EDA bank marketing project"
   ```
2. Crea un repositorio vacío en tu cuenta de GitHub (público) y añade el remoto:
   ```bash
   git remote add origin https://github.com/<tu_usuario>/<tu_repo>.git
   git branch -M main
   git push -u origin main
   ```

---

© 2025-09-25 – Proyecto educativo.
