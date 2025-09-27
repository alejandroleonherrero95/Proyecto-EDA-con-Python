def safe_parse_date(s, dayfirst=True):
    """
    Intenta convertir fechas de manera tolerante.
    Si no puede, devuelve NaT sin lanzar warnings.
    """
    try:
        return pd.to_datetime(s, errors="coerce", dayfirst=dayfirst, infer_datetime_format=True)
    except Exception:
        return pd.to_datetime(s, errors="coerce", dayfirst=dayfirst)
