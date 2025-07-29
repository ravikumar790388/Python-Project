import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

# Step 1: Create or Load Some Data
data = {
    'Department': ['Sales', 'Marketing', 'HR', 'IT'],
    'Employees': [10, 8, 4, 6],
    'Performance': [88, 76, 90, 85]
}

df = pd.DataFrame(data)

# Step 2: Plot a Chart
plt.figure(figsize=(6, 4))
plt.bar(df['Department'], df['Performance'], color='skyblue')
plt.title('Department Performance')
plt.ylabel('Score')
plt.savefig("performance_chart.png")
plt.close()

# Step 3: Generate PDF Report
def generate_pdf_report(filename="automated_report.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Company Performance Report")

    # Date
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 70, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Insert Chart
    c.drawImage("performance_chart.png", 50, height - 300, width=400, height=200)

    # Table Header
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 320, "Department Data:")

    # Draw Table
    c.setFont("Helvetica", 10)
    y = height - 340
    for index, row in df.iterrows():
        text = f"{row['Department']:10} | Employees: {row['Employees']} | Performance: {row['Performance']}"
        c.drawString(50, y, text)
        y -= 20

    c.save()
    print("Report saved as", filename)

generate_pdf_report()
