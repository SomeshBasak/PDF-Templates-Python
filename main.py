from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation = "P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,0,254)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)

    for y in range(20,298,10):
        pdf.line(x1=10,y1=y, x2=200,y2=y)

    # Set the footer
    pdf.ln(266)
    pdf.set_font(family="Times", style="B", size=8)
    pdf.set_text_color(100, 20, 200)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1 ):
        pdf.add_page()
        # Set the footer
        pdf.ln(278)
        pdf.set_font(family="Times", style="B", size=8)
        pdf.set_text_color(100, 20, 200)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        for y in range(20, 298, 10):
            pdf.line(x1=10, y1=y, x2=200, y2=y)

pdf.output("output.pdf")
