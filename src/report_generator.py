import pandas as pd

def generate_report(file_path):
    try:
        df = pd.read_csv(file_path, parse_dates=['Date'])

        print("\n📊 Basic Report Summary\n")
        print("Date Range:", df['Date'].min().date(), "to", df['Date'].max().date())
        print("\n--- Summary Statistics ---")
        print(df.describe())
        print("\n--- Missing Values ---")
        print(df.isnull().sum())
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    generate_report("../data/sample_data.csv")
