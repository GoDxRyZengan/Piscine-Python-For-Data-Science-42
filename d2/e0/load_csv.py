import pandas as pd

def load(path: str) -> pd.DataFrame:
    try:
        if not (path.endswith(".csv")):
            raise ValueError('File must be of .csv extention')
        if not isinstance(path, str):
            raise TypeError(f"{path}: is not valid a path")
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return (df)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    return None