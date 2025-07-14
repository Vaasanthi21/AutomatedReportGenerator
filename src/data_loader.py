import pandas as pd
import os

def load_or_create_data(filepath):
    # If file doesn't exist or is empty, create dummy data
    if not os.path.exists(filepath) or os.stat(filepath).st_size == 0:
        print("[INFO] File not found or empty. Creating sample data...")
        df = pd.DataFrame({
            'Date': pd.date_range(start="2022-01-01", periods=5, freq='D'),
            'Revenue': [1000, 1500, 1200, 1300, 1700],
            'Expenses': [500, 700, 600, 650, 800]
        })
        df.to_csv(filepath, index=False)
        print(f"[INFO] Sample data written to {filepath}")
        return df
    else:
        try:
            df = pd.read_csv(filepath)
            print(f"[INFO] Data loaded. Shape: {df.shape}")
            return df
        except Exception as e:
            print(f"[ERROR] Could not read the file: {e}")
            return None

if __name__ == "__main__":
    file_path = "../data/sample_data.csv"
    df = load_or_create_data(file_path)

    if df is not None:
        print(df.head())
