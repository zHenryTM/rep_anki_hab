import pandas as pd


def get_enem_data():
    url = "https://github.com/NiedsonEmanoel/NiedsonEmanoel/raw/main/enem/An%C3%A1lise%20de%20Itens/OrdenarPorTri/gerador/provasOrdernadasPorTri.csv"
    return pd.read_csv(url, encoding='utf-8', decimal=',')