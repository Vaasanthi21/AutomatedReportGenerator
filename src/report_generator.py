import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_report(file_path, output_pdf):
    try:
        df = pd.read_csv(file_path, parse_dates=['Date'])

        # Summary values
        date_range = f"{df['Date'].min().date()} to {df['Date'].max().date()}"
        summary_stats = df.describe().round(2)
        total_revenue = df['Revenue'].sum()
        total_expenses = df['Expenses'].sum()
        net_profit = total_revenue - total_expenses

        # Create PDF
        c = canvas.Canvas(output_pdf, pagesize=A4)
        width, height = A4

        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, height - 50, "📊 Automated Report Summary")

        c.setFont("Helvetica", 12)
        c.drawString(50, height - 90, f"Date Range: {date_range}")
        c.drawString(50, height - 110, f"Total Revenue: ₹{total_revenue}")
        c.drawString(50, height - 130, f"Total Expenses: ₹{total_expenses}")
        c.drawString(50, height - 150, f"Net Profit: ₹{net_profit}")

        # Print table-like summary
        y = height - 190
        c.drawString(50, y, "--- Summary Statistics ---")
        y -= 20

        for col in summary_stats.columns:
            c.drawString(50, y, f"{col}: {summary_stats[col].to_dict()}")
            y -= 40
            if y < 100:
                c.showPage()
                y = height - 50

        c.save()
        print(f"[✅] Report saved to {output_pdf}")

    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    generate_report("../data/sample_data.csv", "../reports/summary_report.pdf")
