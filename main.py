import pandas as pd
from fpdf import FPDF as FP

pdf = FP(orientation="P", unit="mm", format="A4")
data = pd.read_csv("topics.csv")
for index, row in data.iterrows():
	pdf.add_page()
	pdf.set_font(family="Helvetica", style="B", size=24)
	pdf.set_text_color(100, 100, 101)
	pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
	pdf.line(10, 21, 200, 21)

pdf.output(rf"notebook.pdf")
