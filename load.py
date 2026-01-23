import pandas as pd

def load(users):
    df = pd.DataFrame(users)
    df.to_csv("SDW2023_Marketing.csv", index=False)
