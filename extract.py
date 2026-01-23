import pandas as pd

def extract():
    df = pd.read_csv("SDW2023.csv")
    users = df.to_dict(orient="records")
    return users
