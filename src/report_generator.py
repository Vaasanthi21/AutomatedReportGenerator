# src/report_generator.py

import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt
import os

def load_data(filepath):
    return pd.read_csv(filepath, parse_dates=["Date"])

def generate_plot(df, output_path):
    df["Profit"] = df["Revenue"] - df["Expenses"]

    plt.figure(figsize=(10, 5))
    plt.plot(df["Date"], df["Revenue"], label="Revenue", marker='o')
    plt.plot(df["Date"], df["Expenses"], label="Expenses", marker='o')
    plt.plot(df["Date"], df["Profit"], label="Profit", marker='o')
    plt.title("Revenue vs Expenses vs Profit")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.savefig(output_path)
    plt.close()

def generate_pdf_report(df, plot_path, output_pdf):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Automated Financial Report", ln=True, align='C')

    pdf.ln(10)
    pdf.set_font("Arial", "", 12)

    avg_revenue = df["Revenue"].mean()
    avg_expenses = df["Expenses"].mean()
    avg_profit = (df["Revenue"] - df["Expenses"]).mean()

    pdf.cell(0, 10, f"Average Revenue: {avg_revenue:.2f}", ln=True)
    pdf.cell(0, 10, f"Average Expenses: {avg_expenses:.2f}", ln=True)
    pdf.cell(0, 10, f"Average Profit: {avg_profit:.2f}", ln=True)

    pdf.ln(10)
    pdf.image(plot_path, w=180)

    pdf.output(output_pdf)
    print(f"[✅] Report generated: {output_pdf}")

# Run script
if __name__ == "__main__":
    data_path = "../data/sample_data.csv"
    plot_path = "../reports/plot.png"
    report_path = "../reports/financial_report.pdf"

    os.makedirs("../reports", exist_ok=True)

    df = load_data(data_path)
    generate_plot(df, plot_path)
    generate_pdf_report(df, plot_path, report_path)
