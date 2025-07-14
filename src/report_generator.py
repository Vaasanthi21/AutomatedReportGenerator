import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os

def generate_plot(df, image_path):
    plt.figure(figsize=(8, 4))
    plt.plot(df['Date'], df['Revenue'], label='Revenue', marker='o')
    plt.plot(df['Date'], df['Expenses'], label='Expenses', marker='x')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.title('Revenue vs Expenses Over Time')
    plt.legend()
    plt.tight_layout()
    plt.savefig(image_path)
    plt.close()

def generate_report(data_path, output_pdf):
    try:
        df = pd.read_csv(data_path, parse_dates=['Date'])

        # Create plot image
        image_path = "../reports/revenue_plot.png"
        generate_plot(df, image_path)

        # Summary
        total_revenue = df['Revenue'].sum()
        total_expenses = df['Expenses'].sum()
        net_profit = total_revenue - total_expenses
        date_range = f"{df['Date'].min().date()} to {df['Date'].max().date()}"

        # Create PDF
        c = canvas.Canvas(output_pdf, pagesize=A4)
        width, height = A4

        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, height - 50, "📊 Financial Report")

        c.setFont("Helvetica", 12)
        c.drawString(50, height - 80, f"Date Range: {date_range}")
        c.drawString(50, height - 100, f"Total Revenue: ₹{total_revenue}")
        c.drawString(50, height - 120, f"Total Expenses: ₹{total_expenses}")
        c.drawString(50, height - 140, f"Net Profit: ₹{net_profit}")

        # Insert plot image
        c.drawImage(ImageReader(image_path), 50, height - 400, width=500, height=250)

        c.save()
        print(f"[✅] PDF report with graph saved to: {output_pdf}")

    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    generate_report("../data/sample_data.csv", "../reports/report_with_graph.pdf")
