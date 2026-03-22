import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_and_preprocess_data(path: str):
    df = pd.read_csv(path)
    y = df["label"].astype(int).values
    X = df.drop(columns=["label"]).values
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X)
    return X, y
